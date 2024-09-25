import unittest
import pandas as pd
from model import TimeSeriesModel
from utils import load_data, preprocess_data

class TestTimeSeriesModel(unittest.TestCase):
    def setUp(self):
        self.model = TimeSeriesModel()
        data = load_data('data/time_series.csv')
        self.data = preprocess_data(data)
        self.model.train(self.data)

    def test_forecast(self):
        predictions = self.model.forecast(5)
        self.assertEqual(len(predictions), 5)

if __name__ == '__main__':
    unittest.main()
