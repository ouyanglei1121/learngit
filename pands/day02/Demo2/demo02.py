import pandas as pd
import numpy as np
data = pd.read_csv('student.txt')
print(data)
date = pd.date_range('20190802', periods=6)
df = pd.DataFrame(np.random.randn(6, 5), index=date, columns=['a', 'b', 'c ', 'd', 'e'])
df.to_excel('student.xls')

