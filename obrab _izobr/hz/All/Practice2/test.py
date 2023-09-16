import cv2
import numpy as np
# _1_ Прочитайте изображение в формате LAB
_source_img_1 = cv2.imread('./_images/1.jpg')
_source_img_2 = cv2.imread('./_images/2.jpg')
_lab_color_img_1 = cv2.cvtColor(_source_img_1.copy(), cv2.COLOR_BGR2LAB)
_lab_color_img_2 = cv2.cvtColor(_source_img_2.copy(), cv2.COLOR_BGR2LAB)
cv2.imwrite('./_images/results/_1_lab_color_img_1.png', _lab_color_img_1)
cv2.imwrite('./_images/results/_1_lab_color_img_2.png', _lab_color_img_2)