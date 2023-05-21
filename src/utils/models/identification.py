import numpy as np
from statsmodels.tsa.arima.model import ARIMA


def get_BIC_matrix(signal, ar_span=20, ma_span=20):
    BIC_matrix = np.zeros((ar_span, ma_span))

    for ar_order in range(1, ar_span+1):
        for ma_order in range(1, ar_span+1):
            BIC = ARIMA(signal, order=(ar_order, 0, ma_order)).fit().bic
            BIC_matrix[ar_order-1][ma_order-1] = BIC

    return BIC_matrix


def get_order_from_BIC_matrix(matrix):

    ma_order = np.argmin(matrix) % matrix.shape[1]
    ar_order = np.argmin(matrix) // matrix.shape[0]

    return (ar_order, ma_order)
