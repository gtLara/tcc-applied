import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from utils.models.identification import get_order_from_BIC_matrix
from utils.visual.configure import get_configs
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

mpl.rcParams = get_configs()


def plot_acfs(signal: pd.Series | np.ndarray) -> None:
    plt.style.use("ggplot")
    ax = plt.subplots(2, 1)

    plot_acf(signal, ax=ax[1][0])
    plot_acf(signal, ax=ax[1][1])

    plt.savefig("plots/model_identification.pdf")
    plt.close()


def visualize_BIC_matrix(matrix: np.ndarray, highlight_min=False):
    plt.style.use("default")

    if not highlight_min:
        plt.imshow(matrix)
    else:
        plt.imshow(matrix == np.min(matrix))

    plt.title("Matriz BIC")

    plt.xticks([])
    plt.yticks([])

    plt.xlabel("")
    plt.ylabel("")

    ar_order, ma_order = get_order_from_BIC_matrix(matrix)

    if highlight_min:
        plt.text(ma_order, ar_order, f"({ar_order}, {ma_order})")
        plt.savefig("plots/order_highlighted_BIC_matrix.png", dpi=150)
    else:
        plt.savefig("plots/BIC_matrix.png", dpi=150)
