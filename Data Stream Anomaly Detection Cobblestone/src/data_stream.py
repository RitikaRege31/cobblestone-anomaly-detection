# src/data_stream.py
import numpy as np

# Parameters for data stream generation
STREAM_LENGTH = 1000       # Total number of data points to generate
NOISE_LEVEL = 0.5          # Standard deviation of random noise added to the stream
SEASONAL_AMPLITUDE = 5     # Amplitude for the sinusoidal seasonal pattern
SEASONAL_PERIOD = 50       # Period of the seasonal sinusoidal pattern

def data_stream_simulation():
    """
    Generates a synthetic data stream with periodic patterns, random noise, and occasional anomalies.
    
    Yields:
        float: The next data point in the simulated data stream.
    """
    for i in range(STREAM_LENGTH):
        # Generate a sinusoidal seasonal pattern and add random noise
        seasonal_value = SEASONAL_AMPLITUDE * np.sin(2 * np.pi * i / SEASONAL_PERIOD)
        noise = np.random.normal(0, NOISE_LEVEL)
        
        # Occasionally inject an anomaly with a higher value
        if np.random.rand() < 0.02:  # 2% chance of anomaly
            yield seasonal_value + noise + np.random.uniform(10, 20)
        else:
            yield seasonal_value + noise
