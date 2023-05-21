from typing import Union
import numpy as np
import pandas as pd
from utils.models.trend import get_polynomial_trend, get_detrended_signal
from utils.models.seasonality import get_stochastic_seasonal_component
from utils.signals.correlation import infer_period


def get_decomposition(signal: np.ndarray | pd.Series,
                      polynomial_trend_degree: int,
                      sampling_period: int,
                      visual: bool = True):

    trend = get_polynomial_trend(signal=signal,
                                 degree=polynomial_trend_degree)

    period = infer_period(signal-trend, period_estimate=60,
                          sampling_period=sampling_period)

    trended_seasonal_pattern = get_stochastic_seasonal_component(signal,
                                                                 period,
                                                                 visual)

    seasonal_pattern = get_detrended_signal(signal=trended_seasonal_pattern,
                                            trend_degree=polynomial_trend_degree)

    residual = signal - trend - seasonal_pattern

    results = {"trend": trend,
               "seasonal": seasonal_pattern,
               "residual": residual}

    return results
