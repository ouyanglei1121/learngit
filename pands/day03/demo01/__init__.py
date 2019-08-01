#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: ouyang lei time:2019/7/31
import pandas as pd
import numpy as np
left = pd.DataFrame({'key1': ['k0', 'k0', 'k1', 'k2'],
                    'key2': ['k0', 'k1', 'k0', 'k1'],
                     'a': ['a0', 'a1', 'a2', 'a3'],
                     'b': ['b0', 'b1', 'b2', 'b3']})

right = pd.DataFrame({'key1': ['k0', 'k1', 'k1', 'k2'],
                     'key2': ['k0', 'k0', 'k0', 'k0 '],
                      'c': ['c0', 'c1', 'c2', 'c3'],
                      'd': ['d0', 'd1', 'd2', 'd3']
                      })

print(left)
print(right)
# how = {'left', 'right', 'outer', 'inner'}
res1 = pd.merge(left, right, on=['key1', 'key2'], how='left', indicator=True)  # indicator=True显示怎么合并的  how='left'根据左边的‘key1’，‘key2’来合并
print(res1)
res2 = pd.merge(left, right, on=['key1', 'key2'], how='outer', indicator='indicator_column')  # indicator='indicator_column'自定义一个名字
print(res2)
res3 = pd.merge(left, right, left_index=True, right_index=True, how='outer')  # left_index=True, right_index=True  根据左边和右边的索引拼接
print(res3)


