'''Форма - это ключевой параметр при работе с n-мерными массивами
.shape()
'''
import numpy as np

marks = np.array([
    29.3, 42.5, 38.0, 0.1, 12.5, 99.9,
    9.2, 56.5, 18.3, 64.2, 95.1, 22.2
]).reshape(2, 2, 3)

print(marks.shape)
print(marks)

np.swapaxes()
