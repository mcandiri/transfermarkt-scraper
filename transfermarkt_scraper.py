import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
from typing import List, Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def fetch_page_content(url: str) -> bytes:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        return response.content
    except requests.RequestException as e:
        logging.error(f'Request failed: {e}')
        return None

def parse_transfers(content: bytes, year: int) -> List[Tuple[str, str, str]]:
    if content is None:
        logging.error('No content to parse')
        return []

    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', {'class': 'items'})

    if not table:
        logging.warning(f'No transfer table found for year {year}')
        return []

    transfer_list = []
    for row in table.find_all('tr', {'class': ['odd', 'even']}):
        cells = row.find_all('td')
        if len(cells) > 15:
            player_name = cells[3].text.strip()
            left_team = cells[10].text.strip() if cells[5].text.strip() else 'Unknown'
            joined_team = cells[14].text.strip() if cells[6].text.strip() else 'Unknown'
            transfer_list.append((player_name, left_team, joined_team))

    return transfer_list

def save_transfers(transfers: List[Tuple[str, str, str]], year: int):
    df = pd.DataFrame(transfers, columns=['Player', 'Left Team', 'Joined Team'])
    file_name = f'{year}-transfers.csv'
    df.to_csv(file_name, index=False)
    logging.info(f'Saved transfers to {file_name}')

def scrape_transfers_for_years(start_year: int, end_year: int, pages_per_year: int):
    for year in range(start_year, end_year - 1, -1):
        all_transfers = []
        for page_number in range(1, pages_per_year + 1):
            logging.info(f'Scraping year {year}, page {page_number}')
            url = f"https://www.transfermarkt.com/transfers/saisontransfers/statistik?land_id=0&ausrichtung=&spielerposition_id=&altersklasse=&leihe=&transferfenster=&saison_id={year}&plus=1&page={page_number}"
            content = fetch_page_content(url)
            transfers = parse_transfers(content, year)
            all_transfers.extend(transfers)     
            
        if all_transfers:
            save_transfers(all_transfers, year)
        else:
            logging.warning(f'No transfers found for year {year}')
            
            
if __name__ == '__main__':
    start_year = 2023 
    end_year = 2023 
    pages_per_year = 80  
    scrape_transfers_for_years(start_year, end_year, pages_per_year)           
            
            
            
