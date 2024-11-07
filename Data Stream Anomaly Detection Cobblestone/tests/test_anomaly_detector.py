# tests/test_anomaly_detector.py
import unittest
from src.anomaly_detector import ZScoreAnomalyDetector

class TestZScoreAnomalyDetector(unittest.TestCase):
    def test_no_anomalies_in_constant_stream(self):
        detector = ZScoreAnomalyDetector(window_size=5, threshold=3.0)
        # Constant stream, should return False for all detections
        for _ in range(10):
            self.assertFalse(detector.detect(1.0))
    
    def test_detects_anomaly_in_spike(self):
        detector = ZScoreAnomalyDetector(window_size=5, threshold=3.0)
        # Normal data
        for _ in range(5):
            detector.detect(1.0)
        # Spike, should return True
        self.assertTrue(detector.detect(10.0))

    def test_handles_division_by_zero(self):
        detector = ZScoreAnomalyDetector(window_size=5, threshold=3.0)
        # Detect should handle case with all identical values without crashing
        for _ in range(5):
            detector.detect(1.0)
        self.assertFalse(detector.detect(1.0))  # Should not throw division by zero error

if __name__ == "__main__":
    unittest.main()
