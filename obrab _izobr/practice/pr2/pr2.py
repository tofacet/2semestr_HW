import cv2
import numpy as np

#1. Исходные изображения
##Считываем исходные изображения
orig_img_01 = cv2.imread('pr2_img/01.jpg')
orig_img_02 = cv2.imread('pr2_img/02.jpg')
orig_img_01_rgb = cv2.cvtColor(orig_img_01.copy(), cv2.COLOR_BGR2LAB)
orig_img_02_rgb  = cv2.cvtColor(orig_img_02.copy(), cv2.COLOR_BGR2LAB)

#2. ЧБ изображения
##Функция преобраования в черно-белое изображение
def monochrome(input_lab_img):
    width, height, depth = input_lab_img.shape
    for i in range(width):
        for j in range(height):
            l, a, b = input_lab_img[i, j]
            gray = 255 if (l > 255 / 2) else 0
            input_lab_img[i, j] = (gray, gray, gray)
    return input_lab_img

#Применение функции к исходным изображениям
mono_01 = monochrome(orig_img_01_rgb.copy())
mono_02 = monochrome(orig_img_02_rgb.copy())

#Запись в папку черно-белых изображений
cv2.imwrite('pr2_img/01_bw.png', mono_01)
cv2.imwrite('pr2_img/02_bw.png', mono_02)

# 3.Преобразование изображения в негатив
negative_01 = 255 - mono_01.copy()
negative_02 = 255 - mono_02.copy()
cv2.imwrite('pr2_img/01_neg.png', negative_01)
cv2.imwrite('pr2_img/02_neg.png', negative_02)

#4. Логарифмические преобразования 
#Функция логарифмического преобразования 
def log(r, c):
    max = np.max(r)
    log_max = np.log(1 + max) 
    s = c * (np.log(1 + r)/log_max)
    s = np.array(s, dtype=np.uint8)
    return s

#Применение функции к изображению
log_01_x = log(orig_img_01.copy(), 255)
log_01_y = log(orig_img_01.copy(), 100)
log_02_x = log(orig_img_02.copy(), 255)
log_02_y = log(orig_img_02.copy(), 100)

#запись изображений в папку 
cv2.imwrite('pr2_img/01_log_x.png', log_01_x)
cv2.imwrite('pr2_img/01_log_y.png', log_01_y)
cv2.imwrite('pr2_img/02_log_x.png', log_02_x)
cv2.imwrite('pr2_img/02_log_y.png', log_02_y)

## 5. Степенное преобразование 

#Функция степенного преобразования
def degree(r, y):
    table = np.array([((i / 255.0) ** y) * 255 for i in np.arange(0,256)]).astype("uint8")
    corrected_gamma = cv2.LUT(r, table)
    return corrected_gamma

#Применение функции к изображениям 
#γ>1
deg_01_x = degree(orig_img_01.copy(), 1.5)
#γ<1
deg_01_y= degree(orig_img_01.copy(), 0.5)
#γ>1
deg_02_x = degree(orig_img_02.copy(), 1.5)
#γ<1
deg_02_y= degree(orig_img_02.copy(), 0.5)

#запись изображений в папку
cv2.imwrite('pr2_img/01_deg_x.png', deg_01_x)
cv2.imwrite('pr2_img/01_deg_y.png', deg_01_y)
cv2.imwrite('pr2_img/02_deg_x.png', deg_02_x)
cv2.imwrite('pr2_img/02_deg_y.png', deg_02_y)


#6. Кусочно-линейное преобразование
#Функция Кусочно-линейного преобразования
def sl(img, r1, s1, r2, s2):
    def pl(x):
        if x < r1:
            return (s1 / r1) * x
        elif r1 <= x < r2:
            return ((s2 - s1) / (r2 - r1)) * (x - r1) + s1
        else:
            return ((255 - s2) / (255 - r2)) * (x - r2) + s2
    table = np.array([pl(i) for i in range(256)]).astype('uint8')
    return cv2.LUT(img, table)
#Применение функции к изображениям
sl_01 = sl(orig_img_01.copy(), 15, 0, 230, 255)
sl_02 = sl(orig_img_02.copy(), 15, 0, 230, 255)
#Запись изображений в папку
cv2.imwrite('pr2_img/01_sl.png', sl_01)
cv2.imwrite('pr2_img/02_sl.png', sl_02)

## 7. Вырезание уровней изображения
#Функция вырезания уровней 
def cut(input_img, number_channel):
    width, height, channels = input_img.shape
    for i in range(width):
        for j in range(height):
            color_rgb = input_img[i, j]
            for c in range(channels):
                if (number_channel != c):
                    color_rgb[c] = 0
            input_img[i, j] = color_rgb
    return input_img
#Концертация изображения в цвета RGB
cut_rgb= cv2.cvtColor(orig_img_01, cv2.COLOR_BGR2RGB)
#Применение функции к изображению
l_r= cut(cut_rgb.copy(), 2)
l_g = cut(cut_rgb.copy(), 1)
l_b = cut(cut_rgb.copy(), 0)
#Запись изображений в папку 
cv2.imwrite('pr2_img/cut_l_r.png', l_r)
cv2.imwrite('pr2_img/cut_l_g.png', l_g)
cv2.imwrite('pr2_img/cut_l_b.png', l_b)


