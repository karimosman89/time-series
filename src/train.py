from model import TimeSeriesModel
from utils import load_data, preprocess_data

data = load_data('data/time_series.csv')
data = preprocess_data(data)

ts_model = TimeSeriesModel()
ts_model.train(data)

ts_model.save_model('model.pkl')
