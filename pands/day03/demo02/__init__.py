import pandas as pd
import numpy as np

boys = pd.DataFrame({'k': ['k0', 'k1', 'k2'],
                     'age': [1, 2, 3],
                     'age1': [1, 2, 3]})
girls = pd.DataFrame({'k': ['k0', 'k0', 'k3'],
                      'age': [4, 5, 6],
                      'age1': [1, 2, 3]})
print(boys)
print(girls)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)