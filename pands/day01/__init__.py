import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 6, np.nan, 44, 1])  # 利用数组创建Series类型的数据
print('s:', s)

dates = pd.date_range('20190729', periods=4)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=['a', 'b', 'c', 'd', 'e', 'f'], columns=dates)  # 使用array创建DataFrame类型的数据
print(df)

de = pd.date_range(2, 19, periods=5, name=['a', 'b'])
print(de)

df2 = pd.DataFrame({'A': 1,
                    'B': pd.Timestamp('20190729'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})  # 用字典创建DataFrame类型的数据
print('df2 = ', df2)
print('df2.dtypes = ', df2.dtypes)
print('df2.index = ', df2.index)
print('df2.columns = ', df2.columns)
print('df2.values = ', df2.values)
print('df2.describe() = ', df2.describe())
print('df2.T = ', df2.T)
print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_index(axis=0, ascending=False))
print(df2.sort_index(axis=0, ascending=True))


dates = pd.date_range('20190801', periods=6)
df = pd.DataFrame(np.random.randn(6, 5), index=dates, columns=['a', 'b', 'c', 'd', 'e'])
print(df)
print('------------四种数字的筛选---------------------')
print(df['a'])
print('--------------------------------------')
print(df.a)
print('--------------------------------------')
print(df[1:3])
print('-------------纯标签-------------------')
print(df['20190803':'20190805'])
print('--------------------------------------')
print(df.loc[:, ['a', 'c']])
print('--------------------------------------')
print(df.loc['20190803':, ['a', 'c']])
print('-------------纯索引--------------------')
print(df.iloc[[1, 3], 1:3])
print('--------------------------------------')
print(df)
print('-------------混合--------------------')
print(df.ix[[1, 3], 'a': 'd'])
print('--------------------------------------')
print(df[df.a > 0.5])
