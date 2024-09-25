from model import TimeSeriesModel

ts_model = TimeSeriesModel()
ts_model.load_model('model.pkl')

forecast_steps = 5
predictions = ts_model.forecast(forecast_steps)
print(predictions)
