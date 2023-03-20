from utils.models.trend import get_detrended_signal
from utils.data.write import write_signal
import pickle

with open("data/interim/processed_signal.pkl", "rb") as file:
    signal = pickle.load(file)

detrended_signal = get_detrended_signal(signal=signal,
                                        trend_degree=2)

write_signal(detrended_signal)
