# src/anomaly_detector.py
import numpy as np
from collections import deque

class ZScoreAnomalyDetector:
    """
    Detects anomalies in a data stream based on the Z-score method.
    
    Attributes:
        window_size (int): Number of recent data points used to calculate mean and std deviation.
        threshold (float): Z-score threshold above which a data point is flagged as an anomaly.
    """
    def __init__(self, window_size=50, threshold=3.0):
        """
        Initializes the anomaly detector with a specified window size and threshold.
        
        Args:
            window_size (int): Number of data points for the rolling window.
            threshold (float): Z-score threshold for anomaly detection.
        """
        self.window_size = window_size
        self.threshold = threshold
        self.data_window = deque(maxlen=window_size)
    
    def detect(self, new_value):
        """
        Determines if a new data point is an anomaly.
        
        Args:
            new_value (float): The new data point to evaluate.
        
        Returns:
            bool: True if the new value is an anomaly, False otherwise.
        """
        # Add new value to the rolling window
        self.data_window.append(new_value)
        
        # Wait until the window is full
        if len(self.data_window) < self.window_size:
            return False  # Insufficient data
        
        # Calculate the mean and standard deviation of the rolling window
        mean = np.mean(self.data_window)
        std_dev = np.std(self.data_window)
        
        # Handle cases where the standard deviation is zero
        if std_dev == 0:
            return False
        
        # Calculate the Z-score
        z_score = (new_value - mean) / std_dev
        return abs(z_score) > self.threshold
