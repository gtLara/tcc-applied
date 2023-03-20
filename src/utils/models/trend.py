import numpy as np
from numpy.polynomial import Polynomial


def get_polynomial_trend(signal: np.array, degree: int) -> np.array:
    """
    Fits polynomial trend on time series.

    :param signal: Input signal
    :type signal: np.array
    :param degree: Degree of polynomial
    :type degree: int
    :return: Array corresponding to polynomial fit over the input signal
    :rtype: np.array
    """

    domain = np.arange(len(signal))
    polynomial = Polynomial.fit(x=domain, y=signal, deg=degree)
    _, trend = polynomial.linspace(n=len(signal))

    return trend


def get_detrended_signal(signal: np.array, trend_degree: int = 0) -> np.array:
    """
    Removes polynomial trend from time series.

    :param signal: Input signal
    :type signal: np.array
    :param degree: Degree of trend polynomial
    :type degree: int
    :return: Detrendted signal
    :rtype: np.array
    """

    trend = get_polynomial_trend(signal, trend_degree)

    return signal - trend
