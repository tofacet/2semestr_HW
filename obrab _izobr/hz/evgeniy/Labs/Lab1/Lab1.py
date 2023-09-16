import numpy as np
import cv2
import scipy as sp
import matplotlib.pyplot as plt
from skimage.io import imread, imshow, imsave
from skimage import data, img_as_float

# Изображения

# 1. Подобрать изображения (из практической 2)
INIT_IMG_1 = cv2.imread('img/init/01.jpg')
INIT_IMG_2 = cv2.imread('img/init/02.tif')
INIT_IMG_3 = cv2.imread('img/init/03.jpg')

# 2. Перевести изображения в черно-белые
GRAY_IMG_1 = cv2.cvtColor(INIT_IMG_1.copy(), cv2.COLOR_BGR2GRAY)
GRAY_IMG_2 = cv2.cvtColor(INIT_IMG_2.copy(), cv2.COLOR_BGR2GRAY)
GRAY_IMG_3 = cv2.cvtColor(INIT_IMG_3.copy(), cv2.COLOR_BGR2GRAY)

cv2.imwrite('img/dist/1/GRAY_IMG_1.png', GRAY_IMG_1)
cv2.imwrite('img/dist/1/GRAY_IMG_2.png', GRAY_IMG_2)
cv2.imwrite('img/dist/1/GRAY_IMG_3.png', GRAY_IMG_3)

# 3. Вычислить гистограммы

def save_fig(fig, path=''):
    plt.plot(fig)
    plt.savefig(path)
    plt.close()

# Построить гистограмму изображения 

GIST_GRAY_1 = cv2.calcHist([GRAY_IMG_1], [0], None, [256], [0, 256])
GIST_GRAY_2 = cv2.calcHist([GRAY_IMG_2], [0], None, [256], [0, 256])
GIST_GRAY_3 = cv2.calcHist([GRAY_IMG_3], [0], None, [256], [0, 256])

save_fig(GIST_GRAY_1, 'img/dist/1/GIST_GRAY_1.png')
save_fig(GIST_GRAY_2, 'img/dist/1/GIST_GRAY_2.png')
save_fig(GIST_GRAY_3, 'img/dist/1/GIST_GRAY_3.png')

# Провести нормализацию
def normalize(in_img):
    hist_before_1, bins_before_1 = np.histogram(in_img, 256)
    cdf_1 = hist_before_1.cumsum()
    cdf_1 = (cdf_1-cdf_1[0])*255/(cdf_1[-1]-1)
    normalized = np.zeros((384, 495, 1), dtype =np.uint8)
    normalized = cdf_1[GRAY_IMG_1]
    return normalized

NORMALIZED_1 = normalize(GRAY_IMG_1)
GIST_NORM_1, bins_after_1 = np.histogram(NORMALIZED_1, 256)
cv2.imwrite('img/dist/2/NORMALIZED_1.png', NORMALIZED_1)

save_fig(GIST_NORM_1, 'img/dist/2/GIST_NORM_1.png.png')

# Эквализация

EQUALIZED_1 = cv2.equalizeHist(GRAY_IMG_1.copy())
cv2.imwrite('img/dist/2/EQUALIZED_1.png', EQUALIZED_1)
GIST_EQ_1 = cv2.calcHist([EQUALIZED_1], [0], None, [256], [0, 256])
save_fig(GIST_EQ_1, 'img/dist/2/GIST_EQ_1.png')

# Город

# Эквализация

def run_histogram_equalization(image, path_img, path_gist):
    # convert from RGB color-space to YCrCb
    ycrcb_img = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    # equalize the histogram of the Y channel
    ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
    cv2.imwrite(path_img, equalized_img)
    gist_eq = cv2.calcHist([equalized_img], [2], None, [256], [0, 256])
    save_fig(gist_eq, path_gist)

run_histogram_equalization(INIT_IMG_2, 'img/dist/3/EQUALIZED_2.png', 'img/dist/3/GIST_EQ_2.png')

# Степенное преобразование

def deg_rgb(img, y):
    table = np.array([((i / 255.0) ** y) * 255 for i in np.arange(0,256)]).astype("uint8")
    corrected_gamma = cv2.LUT(img, table)
    return corrected_gamma

DEG_LESS_SAT_2 = deg_rgb(INIT_IMG_2.copy(), 0.5)
cv2.imwrite('img/dist/3/DEG_LESS_SAT_2.png', DEG_LESS_SAT_2)
GIST_DEG_LESS_SAT_2 = cv2.calcHist([DEG_LESS_SAT_2], [2], None, [256], [0, 256])
save_fig(GIST_DEG_LESS_SAT_2, 'img/dist/3/GIST_DEG_LESS_SAT_2.png')

# Логарифмическое преобразование
LOG_IMG = INIT_IMG_2
LOG_IMG[LOG_IMG==255]=254 # делаем такое преобразование, чтобы 0 не попал под логарифм
LOG_IMG_2=np.asarray(np.rint(255*np.log(1+LOG_IMG)/np.log(255)),dtype=np.uint8)
cv2.imwrite('img/dist/3/GIST_NORM_1.png', LOG_IMG_2) #результат логарифмического преобразования
GIST_LOG_2, bins_log_2 = np.histogram(LOG_IMG_2, 256)
save_fig(GIST_LOG_2, 'img/dist/3/GIST_LOG_2.png')

# Кот

# Эквализация

run_histogram_equalization(INIT_IMG_3, 'img/dist/4/EQUALIZED_3.png', 'img/dist/4/GIST_EQ_3.png')

# Степенное преобразование

DEG_LESS_SAT_3 = deg_rgb(INIT_IMG_3.copy(), 0.5)
cv2.imwrite('img/dist/4/DEG_LESS_SAT_3.png', DEG_LESS_SAT_3)
GIST_DEG_LESS_SAT_3 = cv2.calcHist([DEG_LESS_SAT_3], [2], None, [256], [0, 256])
save_fig(GIST_DEG_LESS_SAT_3, 'img/dist/4/GIST_DEG_LESS_SAT_3.png')

# Логарифмическое преобразование
LOG_IMG = INIT_IMG_3
LOG_IMG[LOG_IMG==255]=254 # делаем такое преобразование, чтобы 0 не попал под логарифм
LOG_IMG_3=np.asarray(np.rint(255*np.log(1+LOG_IMG)/np.log(255)),dtype=np.uint8)
cv2.imwrite('img/dist/4/GIST_NORM_1.png', LOG_IMG_3) #результат логарифмического преобразования
GIST_LOG_3, bins_log_2 = np.histogram(LOG_IMG_3, 256)
save_fig(GIST_LOG_3, 'img/dist/4/GIST_LOG_3.png')