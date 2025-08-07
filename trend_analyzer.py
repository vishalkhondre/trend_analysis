import pandas as pd

def load_data_from_csv(filename):
    """
    Loads vibration data from a CSV file into a Pandas DataFrame.

    Args:
        filename (str): The name of the CSV file to load.

    Returns:
        pd.DataFrame: The loaded data as a Pandas DataFrame.
    """
    return pd.read_csv(filename)

