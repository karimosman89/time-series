import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    """Load the CSV time series data."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data, n_steps):
    """Preprocess the data into sequences for LSTM."""
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    X, y = [], []
    for i in range(n_steps, len(scaled_data)):
        X.append(scaled_data[i-n_steps:i])
        y.append(scaled_data[i])

    X = np.array(X)
    y = np.array(y)

    return X, y, scaler

def inverse_transform(scaler, data):
    """Inverse the scaling."""
    return scaler.inverse_transform(data)

