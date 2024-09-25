import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Example preprocessing steps
    data['date'] = pd.to_datetime(data['date'])
    data.set_index('date', inplace=True)
    return data
