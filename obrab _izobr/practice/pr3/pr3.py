import matplotlib.pyplot as plt
import numpy as np
import random
import cv2
from matplotlib import pyplot as plt

#Исходные изображения 
orig_img_01 = cv2.imread('img/01.jpg')
orig_img_02 = cv2.imread('img/02.jpg')

#Перевести изображения в черно-белые
bw_01 = cv2.cvtColor(orig_img_01.copy(), cv2.COLOR_BGR2GRAY)
bw_02 = cv2.cvtColor(orig_img_02.copy(), cv2.COLOR_BGR2GRAY)
#Запись в папку черно-белых изображений
cv2.imwrite('img/01_bw.png', bw_01)
cv2.imwrite('img/02_bw.png', bw_02)

#Вычислить гистограммы
bc_01 = cv2.calcHist([bw_01], [0], None, [256], [0, 256])
bc_02 = cv2.calcHist([bw_02], [0], None, [256], [0, 256])
#Отобразим график
plt.plot(bc_01)
plt.show()
#Запишем график в папку
plt.plot(bc_01)
plt.savefig('img/01_bw_bc.png') 
plt.close()
#Отобразим график
plt.plot(bc_02)
plt.show()
#Запишем график в папку
plt.plot(bc_02)
plt.savefig('img/02_bw_bc.png') 
plt.close()

#Нормализация гистограмм
#Вычисление гистограммы набора данных
hist_01, bins_01 = np.histogram(bw_01, 256)
hist_02, bins_02 = np.histogram(bw_02, 256)
#Вычисление cdf
cdf_01 = hist_01.cumsum()
cdf_02 = hist_02.cumsum()

#Формула распределения
cdf_01 = (cdf_01-cdf_01[0])*255/(cdf_01[-1]-1)
cdf_02 = (cdf_02-cdf_02[0])*255/(cdf_02[-1]-1)
cdf_01 = cdf_01.astype(np.uint8)
cdf_02 = cdf_02.astype(np.uint8)

#Генерируем изображение после нормализации гистограммы
img_norm_01 = np.zeros((384, 495, 1), dtype =np.uint8)
img_norm_02 = np.zeros((384, 495, 1), dtype =np.uint8)
img_norm_01 = cdf_01[bw_01]
img_norm_02 = cdf_02[bw_02]


#Записываем нормализированные изображения в папку
cv2.imwrite('img/01_img_norm.png', img_norm_01)
cv2.imwrite('img/02_img_norm.png', img_norm_02)

bc_norm_01, binsa_01 = np.histogram(img_norm_01, 256)
bc_norm_02, binsa_02 = np.histogram(img_norm_02, 256)
#Вывод графика
plt.plot(bc_norm_01)
plt.show()
#Сохранения графика в папку
plt.plot(bc_norm_01)
plt.savefig('img/01_bc_norm.png')
plt.close()
#Вывод графика
plt.plot(bc_norm_02)
plt.show()
#Сохранения графика в папку
plt.plot(bc_norm_02)
plt.savefig('img/02_bc_norm.png')
plt.close()


#Эквализация 
ekv_01 = cv2.equalizeHist(bw_01.copy())
ekv_02 = cv2.equalizeHist(bw_02.copy())
#сохранения изображений в папку
cv2.imwrite('img/01__img_ekv.png', ekv_01)
cv2.imwrite('img/02_img_ekv.png', ekv_02)
#вычисление гистограмм
bc_ekv_01 = cv2.calcHist([ekv_01], [0], None, [256], [0, 256])
bc_ekv_02 = cv2.calcHist([ekv_02], [0], None, [256], [0, 256])

#Вывод графика
plt.plot(bc_ekv_01)
plt.show()
#Сохранения графика в папку
plt.plot(bc_ekv_01)
plt.savefig('img/01_bc_ekv.png')
plt.close()

#Вывод графика
plt.plot(bc_ekv_02)
plt.show()
#Сохранения графика в папку
plt.plot(bc_ekv_02)
plt.savefig('img/02_bc_ekv.png')
plt.close()

# Преобразование гистограм по произвольной функции распределения

func_cdf_01 = hist_01.cumsum()
func_cdf_02 = hist_02.cumsum()

# Произвольная функция распредления
func_cdf_01 = (func_cdf_01 - func_cdf_01[random.randint(0, 256)] + random.randint(0, 256))*255/(func_cdf_01[-1]-1)
func_cdf_02 = (func_cdf_02 - func_cdf_02[random.randint(0, 256)] + random.randint(0, 256))*255/(func_cdf_02[-1]-1)
func_cdf_01 = func_cdf_01.astype(np.uint8)
func_cdf_02 = func_cdf_02.astype(np.uint8)
#Генерируем изображение после нормализации гистограммы
func_norm_01 = np.zeros((384, 495, 1), dtype =np.uint8)
func_norm_02 = np.zeros((384, 495, 1), dtype =np.uint8)
func_norm_01 = func_cdf_01[bw_01]
func_norm_02 = func_cdf_02[bw_02]
#записываем изображения в папку
cv2.imwrite('img/01_func_norm.png', func_norm_01)
cv2.imwrite('img/02_func_norm.png', func_norm_02)

bc_func_norm_01, bins_func_01 = np.histogram(func_norm_01, 256)
bc_func_norm_02, bins__func_02 = np.histogram(func_norm_02, 256)

#вывод графика
plt.plot(bc_func_norm_01)
plt.show()
#запись графика в папку
plt.plot(bc_func_norm_01)
plt.savefig('img/01_func_bc.png')
plt.close()
#вывод графика
plt.plot(bc_func_norm_02)
plt.show()
#запись графика в папку
plt.plot(bc_func_norm_02)
plt.savefig('img/02_func_bc.png')
plt.close() 