'''
Gaussian - непрерывные признаки и нормальное распределение
Multinominal - дискретные признаки
Bernoulli - двоичные дискретные признаки
'''
from sklearn.naive_bayes import GaussianNB
import numpy as np

curve_center = 80
marks = np.array([72, 58, 30, 51, 18, 90, 12, 88, 5, 100])  # форма (10,), тип int64


def curve(array):
    avg = array.mean()
    # медиана за работу
    error = curve_center - avg  # форма (1,)
    # разница между средним баллом и средней оценкой за курсовую работу
    new_marks = array + error
    return np.clip(new_marks, array, 100)


print(curve(marks))

'''
Векторизация - процесс выполнения одной и той же операции
одинаково для каждого элемента массива. 

Вещание - расширение двух массивов разной формы
'''
