
import numpy as np
import cv2
import matplotlib.pyplot as plt

#исходное изображение 
test_img = cv2.imread('img/test.jpg')

#Чрно-белое изображение 
bw_img = cv2.cvtColor(test_img.copy(), cv2.COLOR_BGR2GRAY)

#запись черно-белого изображения в папку
cv2.imwrite('img/bw_img.png', bw_img)

# Вычислить гистограмму
bc_test = cv2.calcHist([bw_img], [0], None, [256], [0, 256])

#Отобразим график
plt.plot(bc_test)
plt.show()
#Запишем график в папку
plt.plot(bc_test)
plt.savefig('img/bc_test.png') 
plt.close()

#Нормализация гистограмм
#Вычисление гистограммы набора данных
hist_test, bins_test = np.histogram(bw_img, 256)
#Вычисление cdf
cdf_test = hist_test.cumsum()

#Формула распределения
cdf_test = (cdf_test-cdf_test[0])*255/(cdf_test[-1]-1)
cdf_test = cdf_test.astype(np.uint8)

#Генерируем изображение после нормализации гистограммы
img_norm_test = np.zeros((384, 495, 1), dtype =np.uint8)
img_norm_test = cdf_test[bw_img]

#Записываем нормализированные изображения в папку
cv2.imwrite('img/test_img_norm.png', img_norm_test)
#вычисляем гистограмму
bc_norm_test, bins_test1 = np.histogram(img_norm_test, 256)

#Вывод графика
plt.plot(bc_norm_test)
plt.show()
#Сохранения графика в папку
plt.plot(bc_norm_test)
plt.savefig('img/test_bc_norm.png')
plt.close()

#Эквализация 
ekv_test = cv2.equalizeHist(bw_img.copy())

#сохранения изображений в папку
cv2.imwrite('img/test__img_ekv.png', ekv_test)
#вычисление гистограмм
bc_ekv_test = cv2.calcHist([ekv_test], [0], None, [256], [0, 256])

#Вывод графика
plt.plot(bc_ekv_test)
plt.show()
#Сохранения графика в папку
plt.plot(bc_ekv_test)
plt.savefig('img/test_bc_ekv.png')
plt.close()


#Логарифмические преобразование
#Функция логарифмического преобразования 
def log(r, c):
    max = np.max(r)
    log_max = np.log(1 + max) 
    s = c * (np.log(1 + r)/log_max)
    s = np.array(s, dtype=np.uint8)
    return s
#Применение функции к изображению
deg_test_x = log(test_img.copy(), 255)
log_test_y = log(test_img.copy(), 100)

#запись изображений в папку 
cv2.imwrite('img/test_log_x.png', deg_test_x)
cv2.imwrite('img/test_log_y.png', log_test_y)

#рассчитаем гистограммы
bc_deg_x = cv2.calcHist([deg_test_x], [0], None, [256], [0, 256])
bc_log_y = cv2.calcHist([log_test_y], [0], None, [256], [0, 256])

#Вывод графика
plt.plot(bc_deg_x)
plt.show()
#Сохранения графика в папку
plt.plot(bc_deg_x)
plt.savefig('img/bc_deg_x.png')

#Вывод графика
plt.plot(bc_log_y)
plt.show()
#Сохранения графика в папку
plt.plot(bc_log_y)
plt.savefig('img/bc_log_y.png')

#Степенное преобразование 
#Функция степенного преобразования
def degree(r, y):
    table = np.array([((i / 255.0) ** y) * 255 for i in np.arange(0,256)]).astype("uint8")
    corrected_gamma = cv2.LUT(r, table)
    return corrected_gamma

#Применение функции к изображениям 
#γ>1
deg_test_x = degree(test_img.copy(), 1.5)
#γ<1
deg_test_y= degree(test_img.copy(), 0.5)

#запись изображений в папку
cv2.imwrite('img/test_deg_x.png', deg_test_x)
cv2.imwrite('img/test_deg_y.png', deg_test_y)

#рассчитаем гистограммы
bc_deg_x = cv2.calcHist([deg_test_x], [0], None, [256], [0, 256])
bc_deg_y = cv2.calcHist([deg_test_y], [0], None, [256], [0, 256])

#Вывод графика
plt.plot(bc_deg_x)
plt.show()
#Сохранения графика в папку
plt.plot(bc_deg_x)
plt.savefig('img/bc_deg_x.png')

#Вывод графика
plt.plot(bc_deg_y)
plt.show()
#Сохранения графика в папку
plt.plot(bc_deg_y)
plt.savefig('img/bc_deg_y.png')

