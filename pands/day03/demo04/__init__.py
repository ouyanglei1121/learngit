import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# DataFrame
data = pd.DataFrame(np.random.randn(10000, 4), index=np.arange(10000), columns=list("ABCD"))
print(data.head(3))
data = data.cumsum()
# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', 'scatter', 'hexbin', 'pie'

at = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=at)
plt.show()

