from matplotlib import pyplot as plt
import numpy as np

a = 1664525     # Число из группы в телеграмме 1
b = 1013904223  # Число из группы в телеграмме 2
m = 2 ** 64 + 1 # 2 в степени разрядности системы + 1

x = np.linspace(0, 1, 100)  # Генерируем массив равномерного распределения чисел от 0 до 1 в количестве 100 штук
y = []                      # Массив 

# Генерация точек методом ЛКМ
y_last = 0
for i in range(len(x)):
    y_select = (a * y_last + b) % m
    y_last = y_select
    y.append(y_select)

# Выводим график разброса:
print("Распределение ЛКМ")
plt.scatter(x, y, s = 5, c = 'b') # s - ширина точек, c = цвет точек
plt.show()                        # отображаем график

y_norm = []
y_max = max(y)
y_min = min(y)
for _y in y:
    y_select_norm = (_y - y_min)/(y_max - y_min)
    y_norm.append(y_select_norm)

print("Нормированное распределение ЛКМ")
plt.scatter(x, y_norm, s = 5, c = 'g') # s - ширина точек, c = цвет точек
plt.show()                             # отображаем график

y_avg = sum(y_norm) / len(y_norm)
y_disp = sum([(x - y_avg) ** 2 for x in y_norm]) / len(y_norm) # дисперсия
y_s = y_disp ** 0.5                                            # кв. корень из дисперсии — среднеквадратичное отклонение

print("Среднее: ", y_avg)
print("Дисперсия: ", y_disp)
print("Среднеквадратичное отклонение: ", y_s)