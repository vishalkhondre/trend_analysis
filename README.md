# Vibration Sensor Data Simulator and Trend Analysis

This project contains two Python scripts for simulating and analyzing vibration sensor data.

## Description

`vibration_simulator.py`: This script generates a CSV file named `vibration_data.csv` containing simulated vibration data. The data includes a sinusoidal wave, random noise, and a gradual trend to mimic real-world sensor readings over time.

`trend_analyzer.py`: This script reads the `vibration_data.csv` file, calculates a moving average of the vibration amplitudes to identify trends, and then plots both the raw data and the moving average on a graph.

## Setup

1.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the vibration simulator to generate the data:
    ```bash
    python vibration_simulator.py
    ```

2.  Run the trend analyzer to see the results:
