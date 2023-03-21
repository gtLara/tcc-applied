import matplotlib as mpl


def get_configs():
    mpl.rcParams["figure.figsize"] = (8, 5)
    mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=["#131D42", "black",
                                                        "gray"])
    mpl.style.use("ggplot")

    return mpl.rcParams
