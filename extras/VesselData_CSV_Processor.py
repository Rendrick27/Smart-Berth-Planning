import os
import pandas as pd
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

# Define the folders 
input_folder_path = 'AIS_Sines'
output_folder_path = 'CSV'
final_output_folder_path = 'Combined_CSV'

# Create the output folders if they don't exist
os.makedirs(output_folder_path, exist_ok=True)
os.makedirs(final_output_folder_path, exist_ok=True)


def convert_to_csv(filename):
    """
    Converts a text file to a CSV file.

    Parameters:
        filename (str): The name of the file to be converted.

    Returns:
        str: The path of the output CSV file.
    """
    input_file_path = os.path.join(input_folder_path, filename)
    df = pd.read_csv(input_file_path, delimiter='|')
    csv_filename = filename.replace('.txt', '.csv')
    output_file_path = os.path.join(output_folder_path, csv_filename)
    df.to_csv(output_file_path, index=False)
    return output_file_path


def rename_columns(csv_file_path):
    """
    Renames specific columns of a CSV file.

    Parameters:
        csv_file_path (str): The file path of the CSV to modify.

    Returns:
        str: The file path of the modified CSV.
    """
    df = pd.read_csv(csv_file_path)
    df.rename(columns={
        'UTCDate': 'BaseDateTime',
        'long': 'LON',
        'lat': 'LAT',
        'tipo_cod': 'VesselType',
        'comprimento': 'Length',
        'largura': 'Width',
        'calado': 'Draft',
        'SOGKnots': 'SOG',
        'COGDegrees': 'COG',
        'tipo_desc': 'Cargo',
        'ETA': 'ETA',
        'Destination': 'Destination'
    }, inplace=True)
    df.to_csv(csv_file_path, index=False)
    return csv_file_path


def filter_rows(csv_file_path):
    """
    Filters rows based on specific criteria in a CSV file.

    Parameters:
        csv_file_path (str): The file path of the CSV to filter.

    Returns:
        None
    """
    df = pd.read_csv(csv_file_path)
    df_filtered = df[
        (df['Destination'] == 'SINES') & 
        (df['SourceName'] == 'AIS-SINES') & 
        (df['Cargo'] == 'Cargueiro')
    ]
    df_filtered.to_csv(csv_file_path, index=False)


def combine_csv_files(output_folder_path, final_output_folder_path, max_rows_per_file=1000000):
    """
    Combines multiple CSV files into one or more sorted CSV files based on row limits.

    Parameters:
        output_folder_path (str): The path where the individual CSV files are stored.
        final_output_folder_path (str): The path where the combined CSV files should be stored.
        max_rows_per_file (int): The maximum number of rows each combined file should contain.

    Returns:
        None
    """
    combined_df = pd.DataFrame()
    csv_files = [os.path.join(output_folder_path, f) for f in os.listdir(output_folder_path) if f.endswith('.csv')]
    
    file_index = 1
    for csv_file in tqdm(csv_files, desc='Combining CSV files'):
        df = pd.read_csv(csv_file)
        combined_df = pd.concat([combined_df, df])
        
        if len(combined_df) >= max_rows_per_file:
            combined_df.sort_values(by='BaseDateTime', inplace=True)
            output_combined_file = os.path.join(final_output_folder_path, f'dataset_{file_index}.csv')
            combined_df.to_csv(output_combined_file, index=False)
            combined_df = pd.DataFrame()
            file_index += 1
    
    if not combined_df.empty:
        combined_df.sort_values(by='BaseDateTime', inplace=True)
        output_combined_file = os.path.join(final_output_folder_path, f'dataset_{file_index}.csv')
        combined_df.to_csv(output_combined_file, index=False)


if __name__ == '__main__':
    txt_files = [f for f in os.listdir(input_folder_path) if f.endswith('.txt')]
    with Pool(cpu_count()) as pool:
        print('Convert to CSV')
        csv_files = list(tqdm(pool.imap_unordered(convert_to_csv, txt_files), total=len(txt_files)))
        print('Rename columns')
        csv_files = list(tqdm(pool.imap_unordered(rename_columns, csv_files), total=len(csv_files)))
        print('Filter the rows')
        list(tqdm(pool.imap_unordered(filter_rows, csv_files), total=len(csv_files)))

    combine_csv_files(output_folder_path, final_output_folder_path)

    print('All tasks completed')
