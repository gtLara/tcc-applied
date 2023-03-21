import matplotlib.pyplot as plt
from utils.dvc.params import get_params
from utils.decomposition.decomposition import get_decomposition
from utils.data.write import write_signal
import pickle

# TODO: paraeterize signal read like signal write !

with open("data/interim/processed_signal.pkl", "rb") as file:
    signal = pickle.load(file)

params = get_params()

# Original signal sampling rate is 100 Hz

sampling_period = 100 // get_params("load")["decimation_factor"]
polynomial_trend_degree = params["polynomial_trend_degree"]

decomposition_results = get_decomposition(signal, polynomial_trend_degree,
                                          sampling_period)

write_signal(decomposition_results)
