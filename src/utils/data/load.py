"""
Functions for raw data loading.
"""
from typing import Optional, Union
import pickle
import numpy as np
import pandas as pd
from scipy.signal import decimate
from scipy.ndimage import uniform_filter1d


def get_signal(filename="data/raw/motor_current_signals.pkl",
                        decimation_factor: int = 2,
                        moving_average_win_size:
                        Optional[int] = None) -> pd.Series | np.ndarray:
    """
    Loads and processes pseudo-periodic motor current signal.

    :param filename: Data file path. Defaults to
    "data/motor_current_signals.pkl"
    :type filename: str
    :param decimation_factor: Signal downsampling factor, defaults to 2. For
    no downsampling set 'decimation_factor=1'
    :type decimation_factor: int
    :param moving_average_win_size: Moving average filter window size, defaults
    to None in which case the signal is not filtered at all.
    :type moving_average_win_size: int, optional
    :return: Processed pseudo-periodic signal
    :rtype: pd.Series if 'moving_average_window_size=0' else np.ndarray
    """

    with open(filename, "rb") as file:
        data = pickle.load(file)

    start = pd.to_datetime("2021-05-29 16:32")
    end = pd.to_datetime("2021-05-29 16:40")
    signal = data["[1017:3]"][start:end]

    if decimation_factor > 1:
        signal = decimate(signal, decimation_factor)

    if moving_average_win_size:
        signal = uniform_filter1d(signal, size=moving_average_win_size)

    return signal
