
import pandas as pd
import numpy as np
#from scipy import stats
from datetime import datetime
#from sklearn import preprocessing
#from sklearn.model_selection import KFold
#from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#%matplotlib inline
# 

df = pd.read_csv("./data/StuttgartCsvDone/Halbstd-Werte-Stuttgart-Mitte-SZ_1987_D.csv", index_col=[0], sep = ";")
print(df.head())

df.plot(figsize=(18,5))