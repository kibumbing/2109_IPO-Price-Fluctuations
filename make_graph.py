import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

real = pd.read_csv('forGraph.csv')
real = real.T
real = real[1:]

real.plot()
plt.xlabel("days")
plt.ylabel("Stock price / Offering price")
#plt.ylim([0, 4.5])
plt.plot(real, linewidth=1)
plt.legend().remove()
plt.show()