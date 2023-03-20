"""
Functions for writing of data.
"""
import os
import numpy as np
import pandas as pd
import sys
import pickle


def write_signal(signal: np.ndarray | pd.Series):
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


def write_load_output_signal(signal: np.ndarray | pd.Series):
    """
    Write output signal of load stage.

    :param signal: Signal to write as stage output
    :type signal: np.array or pd.Series
    """

    with open("data/interim/processed_signal.pkl", "wb") as file:
        pickle.dump(signal, file)
