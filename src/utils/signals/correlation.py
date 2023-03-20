"""
Functions for correlation analysis
"""
from scipy.signal import correlate
from warnings import warn
import pandas as pd
import numpy as np


# TODO: work out significance level (tolerance)
def get_crosscorrelation(signal_a: np.ndarray | pd.Series,
                         signal_b: np.ndarray | pd.Series,
                         normalize: bool = True,
                         n_lags: int = np.inf) -> np.ndarray:
    """
    Get cross-correlation between two signals. Cross-covariance can be
    calculated by disabling normalization.

    :param signal_a: Input signal
    :type signal_a: np.ndarray | pd.Series
    :param signal_b: Input signal
    :type signal_b: np.ndarray | pd.Series
    :param normalize: Wether to normalize crosscovariance or not, defaults to
    True
    :type normalize: bool
    :return: Cross-correlation (or covariance if 'normalize=False') between
    'signal_a' and 'signal_b'
    """

    cross_correlation = correlate(signal_a, signal_b)

    if n_lags > len(cross_correlation)//2:
        n_lags = np.inf
        warn("Number of lags exceeds correlation length." +
             " Defaulting to complete correlation.")

    if normalize:
        min_signal_length = min(len(signal_a), len(signal_b))
        std_a, std_b = np.std(signal_a), np.std(signal_b)

        cross_correlation /= (min_signal_length * std_a * std_b)

    if n_lags < np.inf:
        center = len(cross_correlation)//2
        cross_correlation = cross_correlation[center-n_lags+1:center+n_lags]

    # TODO: work out lags
    return cross_correlation#, lags


def get_autocorrelation(signal: np.ndarray | pd.Series,
                        n_lags: int = 15,
                        normalize: bool = True,
                        one_sided: bool = True) -> np.ndarray:
    """
    Get auto-correlation of a signal. Auto-covariance can be
    calculated by disabling normalization.

    :param signal: Input signal
    :type signal: np.ndarray | pd.Series
    :param normalize: Wether to normalize autocovariance or not, defaults to
    True
    :type normalize: bool
    :param one_sided: Wether to return one sided autocorrelation or not,
    defaults to True
    :type one_sided: bool
    :return: Auto-correlation (or covariance if 'normalize=False') of
    'signal_a'
    """

    autocorrelation = get_crosscorrelation(signal_a=signal, signal_b=signal,
                                           normalize=normalize,
                                           n_lags=n_lags+1)

    if one_sided:
        center = len(autocorrelation)//2
        autocorrelation = autocorrelation[center:]

    return autocorrelation
