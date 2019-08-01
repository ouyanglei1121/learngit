import numpy as np
import pandas as pd
dates = pd.date_range('20190801', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
df.iloc[3, 2] = np.nan
df.iloc[2, 3] = np.nan
print(df)
print('-------------------丢掉没有填充的数据或丢失的数据-------------------')
print(df.dropna(axis=0, how='any'))  # how={'any', 'all'}  'any' 为只要有一个nan就会处理，'all'为要全部都是nan才会处理 axis=0丢掉的是行
print('-------------------将没有填充的数据或丢失的数据设置为指定的数据-------------------')
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['a', 'b', 'c', 'd'])
df.iloc[3, 2] = np.nan
df.iloc[2, 3] = np.nan
print(df)
print(df.fillna(value=2))  # 将没有填充的数据或丢失的数据设置为指定的数据
print('-------------------检查表格中是否有没有填充的数据或丢失的数据-------------------')
print(df.isnull())
print(np.any(df.isnull()) == True)  # np.any(df.isnull())至少有一个是等于True的
print(df.notnull())



