import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Series
data = pd.Series(np.random.randn(10000), index=np.arange(500, 10500))
data = data.cumsum()
data.plot()
plt.show()


# DataFrame
data = pd.DataFrame(np.random.randn(10000, 4), index=np.arange(10000), columns=list("ABCD"))
print(data.head(3))
data = data.cumsum()
# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', 'scatter', 'hexbin', 'pie'
data.plot()  # 里面有好多参数，请上网查询
plt.show()
