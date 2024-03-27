# Football Transfer Data Scraper
  
This repository contains a Python-based tool for scraping and analyzing
football player transfer data. It automates the collection of player
names, former teams, and new teams from various years, facilitating the
study of trends in football transfers.  
  
## Installation 
  
To set up this project locally, you'll need Python installed on your
system along with a few additional packages. Follow these steps:  
  
Clone the repository:  
git clone https://github.com/mcandiri/transfermarkt-scraper.git  
Navigate to the project directory  
cd transfermarkt-scraper  
Install the required Python packages:  
pip install requests beautifulsoup4 pandas  
  
## Usage  
After installation, you can start scraping football transfer data by
running:  
    ```bash  
    python transfermarkt_scraping.py  
    ```
    
Modify the start_year and end_year parameters in the script as
needed to fetch data for specific years.  
  
 
## Additional Tools

### CSV File Combiner

This repository also includes a Python script `combine_csv_files.py`, which combines multiple CSV files into a single CSV file and cleans the data by removing duplicates and unnamed columns.

#### Usage

To use this script:

1. Ensure you have Python and pandas installed on your system.
2. Place `read_all_files.py` in your desired directory.
3. Run the script with the following command, specifying the path to the folder containing your CSV files and the name of the output file:

```bash
python read_all_files.py /path/to/csv/folder combined_output.csv
```
  
## Features

- Data scraping from trusted football data sources.

- Parsing and cleaning of transfer data.

- Saving data in a structured CSV format for easy analysis.  
    
## Contributing  
  Your contributions are welcome! If you have suggestions or
  improvements, feel free to fork the repository, make your changes, and
  submit a pull request. For major changes, please open an issue first
  to discuss what you would like to change.  
    
## License
  This project is licensed under the MIT License - see the LICENSE file
  for details.  
    
    
    
    
    
    
    
    
    
    
    
    
