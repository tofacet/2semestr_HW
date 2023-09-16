import numpy as np
import matplotlib.pyplot as plt
import cv2

from skimage.io import imread, imshow, imsave
from skimage.color import rgb2gray
from skimage import exposure

INIT_1 = imread('img/1/4_01.jpg', as_gray=True)
INIT_2 = imread('img/2/4_02.jpg', as_gray=True)
INIT_4 = imread('img/4/4_04.jpg', as_gray=True)
INIT_5 = imread('img/5/4_05.jpg', as_gray=True)
INIT_6 = imread('img/6/4_06.jpg', as_gray=True)

IMAGES = [INIT_1, INIT_2, INIT_4, INIT_5, INIT_6]
NUMBERS = [1, 2, 4, 5, 6]

# Для преобразования Фурье использовалась функция из NumPy np.fft.fft2, принимающая двумерный массив, 
# соответствующий светлотам пикселей изображения. 
# Визуализация центрованного спектра осуществлялась с помощью метода np.fft.fftshift

def fft(x):
    return 100 * np.log(np.abs(np.fft.fftshift(np.fft.fft2(x))))

def save(init_img, number):
    plt.imsave('img/{}/RESULT_{}.jpg'.format(number, number), fft(init_img), cmap='gray')

plt.imshow(fft(INIT_1), cmap='gray')

i = 0
for x in IMAGES:
    save(x, NUMBERS[i])
    i+=1

# Невооруженным взглядом можно увидеть некоторые закономерности. В центре спектра часто находится светлая область: 
# она отражает характер «низких гармоник» — больших световых пятен исходного изображения. 
# Удаленные от центра точки на визуализации передают характер «высоких гармоник» — мелких деталей 
# исходника, шумов и линий.

# Частоты в Фурье-преобразовании связаны с изменением светлот в изображении
# 1. Низкие частоты отвечают за плавное изменение светлот
# 2. Высокие частоты характеризуют резкие перепады светлот,
# которым соответствуют границы деталей и шумы