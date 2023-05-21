import pickle
from statsmodels.tsa.stattools import adfuller

with open("data/decomposed/residual.pkl", "rb") as file:
    residual = pickle.load(file)

# test for stationarity

pvalue = adfuller(residual, regression="n")[1]

# take first diff then test for stationarity

# model arma based on AIC, BIC
