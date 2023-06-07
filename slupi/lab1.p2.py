from matplotlib import pyplot as plt

def random_generator_center_sqrt(R0, count_values):
    """
        Генератор случайной последовательности.\n
        Метод срединных квадратов.\n
        R0 - четное число, n — разрядность числа R0 (сколько цифр после запятой)
    """

    result = []
    for i in range(count_values): 
        # Возводим в квадрат - R0 * R0
        square_str = str(R0 ** 2)
        start_index = len(square_str) // 4
        finish_index = start_index + 1 if len(square_str) % 2 else start_index
        R0 = int(square_str[start_index:-finish_index])
        result.append(R0)
    return result

R0, count_values = 5503145745345345345, 100
result = random_generator_center_sqrt(R0, count_values)
print(result)

# Выводим график разброса:
print("Распределение метод срединных квадратов")
plt.scatter(range(0, len(result)), result, s = 5, c = 'b') # s - ширина точек, c = цвет точек
plt.show()                        # отображаем график

# Статистика
# Можно убрать и он попросит добавить
y_norm = []
y_max = max(result)
y_min = min(result)
for _y in result:
    y_select_norm = (_y - y_min)/(y_max - y_min)
    y_norm.append(y_select_norm)

y_avg = sum(y_norm) / len(y_norm)                              # среднее
y_disp = sum([(x - y_avg) ** 2 for x in y_norm]) / len(y_norm) # дисперсия
y_s = y_disp ** 0.5                                            # кв. корень из дисперсии — среднеквадратичное отклонение

print("Среднее: ", y_avg)
print("Дисперсия: ", y_disp)
print("Среднеквадратичное отклонение: ", y_s)