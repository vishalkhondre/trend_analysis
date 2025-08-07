import pandas as pd
import matplotlib.pyplot as plt

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

def plot_data_and_trend(dataframe, title):
    """
    Visualizes the raw vibration data and its moving average.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing the data.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(15, 6))
    plt.plot(dataframe['timestamp'], dataframe['amplitude'], label='Raw Data')
    plt.plot(dataframe['timestamp'], dataframe['moving_average'], label='Moving Average', color='red')
    plt.xlabel('Timestamp')
    plt.ylabel('Amplitude')
    plt.title(title)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    vibration_data = load_data_from_csv('vibration_data.csv')
    calculate_moving_average(vibration_data, 100)
    plot_data_and_trend(vibration_data, 'Vibration Analysis')


