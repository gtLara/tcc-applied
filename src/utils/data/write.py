"""
Functions for writing of data.
"""
import os
import numpy as np
import pandas as pd
import sys
import pickle


def write_signal(signal: np.ndarray | pd.Series | dict):
    """
    Write a signal as the output of a stage. The writing method used is
    according to the caller name and it is expected that it represents a
    stage.

    :param signal: Signal to write as stage output
    :type signal: np.array or pd.Series
    """

    stage_name = os.path.basename(sys.argv[0]).replace(".py", "")

    if stage_name == "load":
        write_load_output_signal(signal)
    if stage_name == "detrend":
        write_detrend_output_signal(signal)
    if stage_name == "decompose":
        write_decomposition_output_signals(signal)


def write_load_output_signal(signal: np.ndarray | pd.Series):
    """
    Write output signal of load stage.

    :param signal: Signal to write as load stage output
    :type signal: np.array or pd.Series
    """

    with open("data/interim/processed_signal.pkl", "wb") as file:
        pickle.dump(signal, file)


def write_detrend_output_signal(signal: np.ndarray | pd.Series):
    """
    Write output signal of detrend stage.

    :param signal: Signal to write as detrend stage output
    :type signal: np.array or pd.Series
    """

    with open("data/interim/detrended_signal.pkl", "wb") as file:
        pickle.dump(signal, file)


def write_decomposition_output_signals(signals: dict):
    """
    Write output signals of decomposition stage.

    :param signals: Dictionary containing results of decomposition
    :type signals: dict
    """

    with open("data/decomposed/trend.pkl", "wb") as file:
        pickle.dump(signals["trend"], file)

    with open("data/decomposed/seasonal_pattern.pkl", "wb") as file:
        pickle.dump(signals["seasonal"], file)

    with open("data/decomposed/residual.pkl", "wb") as file:
        pickle.dump(signals["residual"], file)
