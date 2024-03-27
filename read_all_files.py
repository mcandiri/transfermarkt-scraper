import os
import pandas as pd
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def combine_csv_files(folder_path, output_file):
    """
    Combines all CSV files in the specified folder and cleans the data.
    :param folder_path: Path to the folder containing the CSV files
    :param output_file: Name of the file where the combined and cleaned data will be saved
    """
    try:
        # Find all csv files in the folder
        csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        logging.info(f"Found {len(csv_files)} CSV files in {folder_path}.")

        # Combine all CSV files into one DataFrame
        combined_df = pd.concat([pd.read_csv(os.path.join(folder_path, f)) for f in csv_files])
        logging.info("Combined CSV files.")

        # Remove 'Unnamed' columns and duplicates
        combined_df = combined_df.loc[:, ~combined_df.columns.str.contains('^Unnamed')]
        combined_df = combined_df.drop_duplicates()
        logging.info("Removed unnamed columns and duplicates.")

        # Save the combined data to a CSV file
        combined_df.to_csv(output_file, index=False)
        logging.info(f"Output file saved to {output_file}.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Call the function with parameters
combine_csv_files('/path/to/csv/folder', 'combined_output.csv')
