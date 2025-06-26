import pandas as pd
import os


def load_data(file_path):
    """
    Load data from a CSV file and return a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    data = pd.read_csv(file_path)
    return data

