import copy
import matplotlib as mpl
import matplotlib.pyplot as plt


def get_configs(figsize=(8, 5)):

    params = copy.deepcopy(mpl.rcParams)
    params["figure.figsize"] = figsize
    params["axes.prop_cycle"] = mpl.cycler(color=["#131D42", "black",
                                                             "gray"])
    plt.style.use("ggplot")

    return params
