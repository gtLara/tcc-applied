from typing import Optional
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from utils.visual.configure import get_configs

mpl.rcParams = get_configs()


def plot_autocorrelation(autocorrelation: np.ndarray | pd.Series,
                         tolerance: Optional[float] = None,
                         title: str = "Autocorrelação",
                         path: str = "plots/autocorrelation.png") -> None:

    plt.style.use("ggplot")

    plt.stem(autocorrelation)
    plt.title(title)
    plt.xlabel("Atrasos")
    plt.ylabel("Autocorrelação")

    plt.savefig(path, dpi=150)
    plt.close()
