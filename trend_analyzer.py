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

def calculate_moving_average(dataframe, window_size):
    """
    Calculates a moving average of the 'amplitude' column.

    Args:
        dataframe (pd.DataFrame): The input DataFrame.
        window_size (int): The size of the moving average window.

    """
    dataframe['moving_average'] = dataframe['amplitude'].rolling(window=window_size).mean()


