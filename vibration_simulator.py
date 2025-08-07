import numpy as np
import pandas as pd

def generate_vibration_data(duration_minutes, sampling_rate_hz, base_amplitude, frequency_hz, noise_level):
    """
    Generates simulated vibration sensor data.

    Args:
        duration_minutes (int): The duration of the simulation in minutes.
        sampling_rate_hz (int): The sampling rate of the sensor in Hertz.
        base_amplitude (float): The base amplitude of the vibration.
        frequency_hz (float): The frequency of the vibration in Hertz.
        noise_level (float): The level of random noise to add.

    Returns:
        pd.DataFrame: A DataFrame with 'timestamp' and 'amplitude' columns.
    """
    total_samples = int(duration_minutes * 60 * sampling_rate_hz)
    time = np.linspace(0, duration_minutes * 60, total_samples)
    
    # Generate a sinusoidal wave
    sinusoidal_wave = base_amplitude * np.sin(2 * np.pi * frequency_hz * time)
    
    # Generate random noise
    noise = np.random.normal(0, noise_level, total_samples)
    
    # Generate a gradual trend
    trend = np.linspace(0, 0.5, total_samples)
    
    # Combine the components
    amplitude = sinusoidal_wave + noise + trend
    
    # Create a DataFrame
    timestamps = pd.to_datetime(time, unit='s')
    df = pd.DataFrame({'timestamp': timestamps, 'amplitude': amplitude})
    
    return df

def save_data_to_csv(dataframe, filename):
    dataframe.to_csv(filename, index=False)

if __name__ == "__main__":
    # Parameters for the simulation
    duration = 60  # minutes
    sampling_rate = 100  # Hz
    amplitude = 1.0  # base amplitude
    frequency = 50  # Hz
    noise = 0.1  # noise level

    # Generate and save the data
    vibration_df = generate_vibration_data(duration, sampling_rate, amplitude, frequency, noise)
    save_data_to_csv(vibration_df, "vibration_data.csv")
    print("Vibration data saved to vibration_data.csv")

