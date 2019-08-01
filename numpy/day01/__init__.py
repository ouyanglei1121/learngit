import numpy as np
a = np.array([[1, 2, 3],
             [4, 5, 6],
             [1, 2, 3]])

b = np.arange(9).reshape((3, 3))
print(b)
print(np.min(b, axis=0))
print(np.max(b, axis=1))
print(np.sum(b, axis=1))

a = np.arange(14, 2, -1).reshape((3, 4))
print('-------------------------')
print('a = {0}, b = {1}'.format(a, b))
print('-------------------------')
print(np.sum(a, axis=0))
print(np.mean(a, axis=0))
print(np.argmax(a, axis=0))
print('非0的数')
print(np.nonzero(a))
print('a排序：', np.sort(a, axis=0))
print(np.clip(a, 5, 9))  # a中小于5的所有数都等于5， 大于9的所有的数都等于9，在这之间的数保留原型
print('1111111111111111')
for row in a:
    print(row)

print('2222222222222222222222222222222222222222222')
print(a.flatten())  # 将多维数组打平
for i in a.flat:  # flat会返回一个迭代器
    print(i)
print('=======================array的拼接======================')

a = np.array([1, 2, 3])[np.newaxis, :]
b = np.array([4, 5, 23])[np.newaxis, :]
print(a.shape)
print(b.shape)
c = np.vstack((a, b))  # 只能对两个数组进行拼接
print(c)
print(c.shape)

c = np.hstack((a, b))
print(c.shape)
print(c[np.newaxis, :].shape)  # 增加一个维度
print(np.concatenate((a, b, a, a), axis=0))
print('44444444444444444444444444444444444444444444444')
print(np.concatenate((a, b, a, a), axis=1))   # 可以对多个数组进行拼接

print('=======================array的分割======================')
a = np.arange(12).reshape((3, 4))
print(a)
print(np.split(a, 3, axis=0))  # 均等分割
print(np.split(a, 2, axis=1))  # 均等分割
print(np.array_split(a, 3, axis=1))  # 不均等分割

print(np.vsplit(a, 3))
print('------------------------------------------')
print(np.hsplit(a, 4))
