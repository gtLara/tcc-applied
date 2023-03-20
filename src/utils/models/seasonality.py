"""
Functions for the modelling, implicit or explicit, of seasonality.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from warnings import warn
from statsmodels.tsa.seasonal import seasonal_decompose


def get_seasonal_difference(signal: pd.Series | np.ndarray, period: int,
                            dropna: bool = True) -> \
                            pd.Series | np.ndarray:
    """
    Gets seasonal difference of arbitrary period of a signal.

    :param signal: Signal to differentiate
    :type signal: np.ndarray | pd.Series
    :param period: Period of seasonal difference
    :type period: int
    :param dropna: Wether to remove NaN that inevitably arises from
    differencing operation, defaults to True
    :type dropna: bool
    :return: Seasonally differenced signal
    :rtype: np.ndarray
    """

    diffed_signal = pd.Series(signal).diff(periods=period)

    if dropna:
        diffed_signal = diffed_signal.dropna()

    return diffed_signal.values


# TODO: remove visual from here !! move to visual funcs
def get_stochastic_seasonal_component(signal: np.ndarray | pd.Series,
                                      period: int,
                                      visual: False) -> np.ndarray:
    """
    Gets stochastic seasonal component (as defined by Morettin and Toloi) of
    a signal. This procedure assumes the signal is appropriately detrended and
    the period appropriately determined.

    :param signal: Signal for which to determine stochastic seasonal component
    :type signal: np.ndarray | pd.Series
    :param period: Period of seasonal pattern
    :type period: int
    :return: Stochastic seasonal component
    :rtype: np.ndarray
    """

    n_remainder_samples = len(signal) % period

    if n_remainder_samples == 0:
        integer_multiple_signal = signal
    else:
        integer_multiple_signal = signal[:-n_remainder_samples]
        warn("Signal length is a non integer multiple of period. Trailing " +
             "remainder samples will be discarted.")

    integer_multiple_n_samples = len(integer_multiple_signal)
    n_periods = integer_multiple_n_samples//period

    seasonal_segments = np.array(np.split(integer_multiple_signal, n_periods))

    seasonal_pattern = seasonal_segments.mean(axis=0)

    if visual:
        for s, segment in enumerate(seasonal_segments):
            if s == 0:
                plt.plot(segment, color="red", linestyle="--", alpha=0.5,
                         label="Seasonal Segments")
            else:
                plt.plot(segment, color="red", linestyle="--", alpha=0.5)

        plt.plot(seasonal_pattern, color="black",
                 linewidth=2.5,
                 label="Seasonal Mean Component")

        plt.title("Visualization of Stochastic Seasonal Component Computation")
        plt.legend()

    seasonal_component = np.tile(seasonal_pattern, n_periods)

    if n_remainder_samples != 0:
        seasonal_component = np.concatenate([seasonal_component,
                             seasonal_pattern[:n_remainder_samples]])

    return seasonal_component
