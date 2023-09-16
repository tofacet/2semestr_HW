""" #Установка библиотек в Python py -m pip install ...

#Практическая работа 1
#Используемые библиотеки: colormath, color-science, numpy

#Исходные координаты LAB 9 30 -37
LAB -> LCH 9.0 47.6 309.0 
LCH -> LAB 9.0 30.0 -37.0
LAB -> XYZ 0.0202 0.01 0.053
XYZ -> RGB 0.156 0.0157 0.3008
RGB -> XYZ 0.0224 0.0107 0.0706
XYZ -> LAB 9.5 33.3 -36.3
RGB -> HSB 269.5123 0.9477 0.3008
HSB -> LAB 9.5 33.3 -36.3
RGB -> HSL 269.5123 0.9007 0.1583
HSL -> LAB 9.5 33.3 -36.3

#Расчет deltaE, deltaE_94, deltaE_00
delta LCH-LAB 0 0 0
delta RGB-LAB 3.4 1.8 1.9
delta HSB-LAB 3.4 1.8 1.9
delta HSL-LAB 3.4 1.8 1.9 """

from colormath.color_objects import LabColor, LCHabColor, XYZColor, sRGBColor, HSVColor, HSLColor
from colormath.color_conversions import convert_color
import numpy as np

LAB = LabColor(9, 30, -37)
# Преобразование LAB -> LCH 
LCH = convert_color(LAB, LCHabColor)
print(LCH)
# Обратное преобразование LCH -> LAB
inverse_LCH = convert_color(LCH, LabColor)
print(inverse_LCH)
# Конвертация в XYZ
XYZ = convert_color(LAB, XYZColor)
print (XYZ)
# Преоброзование XYZ -> RGB
RGB = convert_color(XYZ, sRGBColor)
print (RGB)
# Обратное преобразование RGB -> XYZ
inverse_XYZ = convert_color(RGB, XYZColor)
print(inverse_XYZ)
# Обратное преобразование XYZ -> LAB
inverse_RGB = convert_color(inverse_XYZ, LabColor)
print(inverse_RGB)
# Преобразование RGB -> HSB
HSB = convert_color(RGB, HSVColor)
print(HSB)
# Обратное преобразование HSB -> LAB
inverse_HSB = convert_color(HSB, LabColor)
print(inverse_HSB)
# Преобразование RGB -> HSL
HSL = convert_color(RGB, HSLColor)
print(HSL)
# Обратное преобразование HSL -> LAB
inverse_HSL = convert_color(HSL, LabColor)
print(inverse_HSL)

from colour.difference import delta_E_CIE1976, delta_E_CIE1994, delta_E_CIE2000

# Подсчет delta LCH-LAB
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([inverse_LCH.lab_l, inverse_LCH.lab_a, inverse_LCH.lab_b])
print(delta_E_CIE1976(a, b))
print(delta_E_CIE1994(a, b))
print(delta_E_CIE2000(a, b))

# Подсчет delta RGB-LAB
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([inverse_RGB.lab_l, inverse_RGB.lab_a, inverse_RGB.lab_b])
print(delta_E_CIE1976(a, b))
print(delta_E_CIE1994(a, b))
print(delta_E_CIE2000(a, b))

# Подсчет delta HSB-LAB
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([inverse_HSB.lab_l, inverse_HSB.lab_a, inverse_HSB.lab_b])
print(delta_E_CIE1976(a, b))
print(delta_E_CIE1994(a, b))
print(delta_E_CIE2000(a, b))

# Подсчет delta HSL-LAB
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([inverse_HSL.lab_l, inverse_HSL.lab_a, inverse_HSL.lab_b])
print(delta_E_CIE1976(a, b))
print(delta_E_CIE1994(a, b))
print(delta_E_CIE2000(a, b))