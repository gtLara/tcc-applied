import matplotlib as mpl
import matplotlib.pyplot as plt
from utils.visual.configure import get_configs

# TODO: fix this!!
mpl.rcParams = get_configs()

mpl.rcParams["figure.figsize"] = (8, 8)
mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=["#131D42", "black",
                                                    "gray"])
mpl.style.use("ggplot")


def plot_decomposition(decomposition_results: dict):

    trend, seasonal, residual = decomposition_results.values()

    plt.subplot(4, 1, 1)
    plt.plot(trend+seasonal+residual)
    plt.title("Original Signal")

    plt.subplot(4, 1, 2)
    plt.plot(trend)
    plt.title("Trend")

    plt.subplot(4, 1, 3)
    plt.plot(seasonal)
    plt.title("Seasonal")

    plt.subplot(4, 1, 4)
    plt.plot(residual)
    plt.title("Residual")

    plt.tight_layout()

    plt.savefig("plots/decomposition.png", dpi=150)
