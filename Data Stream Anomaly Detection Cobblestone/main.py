# main.py
from src.data_stream import data_stream_simulation
from src.anomaly_detector import ZScoreAnomalyDetector
from src.visualization import real_time_plot

if __name__ == "__main__":
    real_time_plot()
