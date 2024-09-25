import joblib
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

class TimeSeriesModel:
    def __init__(self):
        self.model = None

    def train(self, data):
        self.model = ARIMA(data['value'], order=(5, 1, 0))
        self.model = self.model.fit()

    def forecast(self, steps):
        return self.model.forecast(steps)

    def save_model(self, filename):
        joblib.dump(self.model, filename)

    def load_model(self, filename):
        self.model = joblib.load(filename)
