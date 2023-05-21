from utils.signals.correlation import get_autocorrelation
from utils.visual.correlation import plot_autocorrelation
import numpy as np
import pickle

with open("data/decomposed/residual.pkl", "rb") as file:
    residual = pickle.load(file)

autocorrelation_100lags = get_autocorrelation(residual, n_lags=100)
diff_autocorrelation_100lags = get_autocorrelation(np.diff(residual), n_lags=100)
autocorrelation_complete = get_autocorrelation(residual)

# TODO: include confidence interval

plot_autocorrelation(autocorrelation_100lags,
                     title="Autocorrelação truncada de resíduo de decomposição",
                     path="plots/residual_autocorrelation.png")

plot_autocorrelation(diff_autocorrelation_100lags,
                     title="Autocorrelação truncada de diferença primeira de resíduo de decomposição",
                     path="plots/diff_residual_autocorrelation.png")

plot_autocorrelation(autocorrelation_complete,
                     title="Autocorrelação completa de resíduo de decomposição",
                     path="plots/complete_residual_autocorrelation.png")

