# src/visualization.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .data_stream import data_stream_simulation
from .anomaly_detector import ZScoreAnomalyDetector

WINDOW_SIZE = 50
ANOMALY_THRESHOLD = 3.0

def real_time_plot():
    # Initialize the data stream and anomaly detector
    data_stream = data_stream_simulation()
    anomaly_detector = ZScoreAnomalyDetector(WINDOW_SIZE, ANOMALY_THRESHOLD)
    
    # Lists to store data for plotting
    x_data, y_data, anomalies_x, anomalies_y = [], [], [], []
    
    # Plot setup
    fig, ax = plt.subplots()
    ax.set_ylim(-10, 20)
    line, = ax.plot([], [], lw=1, label="Data Stream")
    scatter = ax.scatter([], [], color='red', label="Anomalies")
    ax.legend()

    # Initialize the plot
    def init():
        line.set_data([], [])
        scatter.set_offsets(np.empty((0, 2)))  # Initialize with an empty 2D array
        return line, scatter
    
    # Update the plot with each frame
    def update(frame):
        # Get the next data point from the stream
        new_value = next(data_stream)
        x_data.append(frame)
        y_data.append(new_value)
        
        # Anomaly detection
        is_anomaly = anomaly_detector.detect(new_value)
        if is_anomaly:
            anomalies_x.append(frame)
            anomalies_y.append(new_value)
        
        # Update plot data
        line.set_data(x_data, y_data)
        scatter.set_offsets(np.c_[anomalies_x, anomalies_y])  # Use 2D array for scatter points
        
        return line, scatter
    
    # Create animation with blit=False to avoid `_resize_id` error
    ani = animation.FuncAnimation(fig, update, frames=range(1000),
                                  init_func=init, blit=False, interval=50)
    plt.show()
