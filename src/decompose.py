import matplotlib.pyplot as plt
from utils.dvc.params import get_params
from utils.models.trend import get_polynomial_trend, get_detrended_signal
from utils.signals.correlation import infer_period
from utils.models.seasonality import get_stochastic_seasonal_component
from utils.data.write import write_signal
import pickle

with open("data/interim/processed_signal.pkl", "rb") as file:
    signal = pickle.load(file)

params = {"polynomial_trend_degree": 2}  # get_params()
sampling_period = 50

# decomposition

trend = get_polynomial_trend(signal=signal,
                             degree=params["polynomial_trend_degree"])

period = infer_period(signal-trend, period_estimate=60,
                      sampling_period=sampling_period)

trended_seasonal_pattern = get_stochastic_seasonal_component(signal, period,
                                                             True)

plt.show()

seasonal_pattern = get_detrended_signal(signal=trended_seasonal_pattern,
                                        trend_degree=params["polynomial_trend_"
                                                            + "degree"])

residual = signal - trend - seasonal_pattern

write_signal(residual)
