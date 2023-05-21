import numpy as np
import pickle
from statsmodels.tsa.stattools import adfuller
from utils.models.identification import get_BIC_matrix\
                                        , get_order_from_BIC_matrix
from utils.visual.identification import visualize_BIC_matrix

with open("data/decomposed/residual.pkl", "rb") as file:
    residual = np.diff(pickle.load(file))

# test for stationarity

pvalue = adfuller(residual, regression="n")[1]

# model arma based on BIC

n_windows = 10
for i in range(0, n_windows):
    start = -1000*(i+1)
    end = -1000*(i) - 1
    window = residual[start:end]
    if i == 0:
        BIC_matrix = get_BIC_matrix(window, 5, 5)/n_windows
    else:
        BIC_matrix += get_BIC_matrix(window, 5, 5)/n_windows

ar_order, ma_order = get_order_from_BIC_matrix(BIC_matrix)

visualize_BIC_matrix(BIC_matrix)
visualize_BIC_matrix(BIC_matrix,
                     highlight_min=False)

# maybe separate into stages, because above procedure will take a longgg time

# model residuals by one step ahead forecasts? (recover existing code)
