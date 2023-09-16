import cv2
import numpy as np

#Считывание исходных изображений

#С маленьким количеством деталей
S1 = cv2.imread('img/S1.jpg')
S2 = cv2.imread('img/S2.jpg')
S3 = cv2.imread('img/S3.jpg')
#С средним количеством деталей
M1 = cv2.imread('img/M1.jpg')
M2 = cv2.imread('img/M2.jpg')
M3 = cv2.imread('img/M3.jpg')
#С большим количеством деталей
L1 = cv2.imread('img/L1.jpg')
L2 = cv2.imread('img/L2.jpg')
L3 = cv2.imread('img/L3.jpg')

#Функции искажения

#Функция размытия изображения
def blur_img(image, kernel_size=(5, 5)):
    return cv2.blur(image, kernel_size)

#Применения функции размытия к изображениям
S1_blur, S2_blur, S3_blur = blur_img(S1), blur_img(S2), blur_img(S3)
M1_blur, M2_blur, M3_blur = blur_img(M1), blur_img(M2), blur_img(M3)
L1_blur, L2_blur, L3_blur = blur_img(L1), blur_img(L2), blur_img(L3)

#Функция имульсного шума(шум соль и перец)
def noise_img(image, probability=0.05, salt_value=255, pepper_value=0):
    noisy_image = np.copy(image)
    h, w, c = noisy_image.shape
    num_pixels = h * w * c
    num_salt = int(num_pixels * probability / 2)
    salt_coords = np.random.randint(0, num_pixels, num_salt)
    noisy_image.flat[salt_coords] = salt_value
    num_pepper = int(num_pixels * probability / 2)
    pepper_coords = np.random.randint(0, num_pixels, num_pepper)
    noisy_image.flat[pepper_coords] = pepper_value
    return noisy_image

#Применения функции шума к изображениям
S1_noise, S2_noise, S3_noise = noise_img(S1_blur), noise_img(S2_blur), noise_img(S3_blur)
M1_noise, M2_noise, M3_noise = noise_img(M1_blur), noise_img(M2_blur), noise_img(M3_blur)
L1_noise, L2_noise, L3_noise = noise_img(L1_blur), noise_img(L2_blur), noise_img(L3_blur)

#Функция сохранения изоражений с потерями
def loss_img(image, output_path, quality=50):
    cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])

#Применение функции к изображениям и запись изображений в папку
S1_dis = loss_img(S1_noise, 'img/S1_dis.jpg', quality=50)
S2_dis = loss_img(S2_noise, 'img/S2_dis.jpg', quality=50)
S3_dis = loss_img(S3_noise, 'img/S3_dis.jpg', quality=50)

M1_dis = loss_img(M1_noise, 'img/M1_dis.jpg', quality=50)
M2_dis = loss_img(M2_noise, 'img/M2_dis.jpg', quality=50)
M3_dis = loss_img(M3_noise, 'img/M3_dis.jpg', quality=50)

L1_dis = loss_img(L1_noise, 'img/L1_dis.jpg', quality=50)
L2_dis = loss_img(L2_noise, 'img/L2_dis.jpg', quality=50)
L3_dis = loss_img(L3_noise, 'img/L3_dis.jpg', quality=50)

#Изображения с искажениями
#С маленьким количеством деталей
S1_dis = cv2.imread('img/S1_dis.jpg')
S2_dis = cv2.imread('img/S2_dis.jpg')
S3_dis = cv2.imread('img/S3_dis.jpg')
#С средним количеством деталей
M1_dis = cv2.imread('img/M1_dis.jpg')
M2_dis = cv2.imread('img/M2_dis.jpg')
M3_dis = cv2.imread('img/M3_dis.jpg')
#С большим количеством деталей
L1_dis = cv2.imread('img/L1_dis.jpg')
L2_dis = cv2.imread('img/L2_dis.jpg')
L3_dis = cv2.imread('img/L3_dis.jpg')

#Функции сопоставления

#Расчет MSE
def MSE(img1, img2):
    return np.sum((img2 - img1)**2) / img1.size

#Расчет PSNR
def PSNR(img1, img2):
    import math
    return math.log10(255/MSE(img1, img2))

#Расчет SSIM
from skimage.metrics import structural_similarity 

#Вывод расчета показателей
#MSE
print("MSE_S1: ", MSE(S1, S1_dis))
print("MSE_S2: ", MSE(S2, S2_dis))
print("MSE_S3: ", MSE(S3, S3_dis), "\n")

print("MSE_M1: ", MSE(M1, M1_dis))
print("MSE_M2: ", MSE(M2, M2_dis))
print("MSE_M3: ", MSE(M3, M3_dis), "\n")

print("MSE_L1: ", MSE(L1, L1_dis))
print("MSE_L2: ", MSE(L2, L2_dis))
print("MSE_L3: ", MSE(L3, L3_dis), "\n"*2)

#PSNR
print("PSNR_S1: ", PSNR(S1, S1_dis))
print("PSNR_S2: ", PSNR(S2, S2_dis))
print("PSNR_S3: ", PSNR(S3, S3_dis), "\n")

print("PSNR_M1: ", PSNR(M1, M1_dis))
print("PSNR_M2: ", PSNR(M2, M2_dis))
print("PSNR_M3: ", PSNR(M3, M3_dis), "\n")

print("PSNR_L1: ", PSNR(L1, L1_dis))
print("PSNR_L2: ", PSNR(L2, L2_dis))
print("PSNR_L3: ", PSNR(L3, L3_dis), "\n"*2)

#SSIM
print("SSIM_S1: ", structural_similarity(S1, S1_dis, channel_axis=2))
print("SSIM_S2: ", structural_similarity(S2, S2_dis, channel_axis=2))
print("SSIM_S3: ", structural_similarity(S3, S3_dis, channel_axis=2), "\n")

print("SSIM_M1: ", structural_similarity(M1, M1_dis, channel_axis=2))
print("SSIM_M2: ", structural_similarity(M2, M2_dis, channel_axis=2))
print("SSIM_M2: ", structural_similarity(M3, M3_dis, channel_axis=2), "\n")

print("SSIM_L1: ", structural_similarity(L1, L1_dis, channel_axis=2))
print("SSIM_L2: ", structural_similarity(L2, L2_dis, channel_axis=2))
print("SSIM_L3: ", structural_similarity(L3, L3_dis, channel_axis=2), "\n")