from colormath.color_objects import  LabColor, LCHabColor, XYZColor, sRGBColor, HSVColor, HSLColor 
from colormath.color_conversions import convert_color
import numpy as np
from colour.difference import delta_E_CIE1976, delta_E_CIE1994, delta_E_CIE2000

#Исходный цвет в пространстве LAB
LAB = LabColor(77, -10, -20)
print("LAB: ", LAB)

#Преобразования цветов из LAB в...
#LCH
LCH = convert_color(LAB, LCHabColor)
print("LCH: ", LCH)
#RGB
RGB = convert_color(LAB, sRGBColor)
print("RGB: ", RGB)
#HSB
HSB = convert_color(LAB, HSVColor)
print("HSB: ", HSB)
#HSI
HSI = convert_color(RGB, HSLColor)
print("HSI: ", HSI)

#Обратное преобразование пространства ... в пространство LAB
#Из LCH 
back_LCH = convert_color(LCH, LabColor)
print("Из LCH в LAB: ", back_LCH)
#Из RGB
back_RGB = convert_color(RGB, LabColor)
print("Из RGB в LAB: ", back_RGB)
#Из HSB
back_HSB = convert_color(HSB, LabColor)
print("Из HSB в LAB: ", back_HSB)
#Из HSI
back_HSI = convert_color(HSI, LabColor)
print("Из HSI в LAB: ", back_HSI)

#Подсчет цветовых различий 

#Различие LCH-LAB
print("РАЗЛИЧИЕ LCH-LAB")
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([back_LCH.lab_l, back_LCH.lab_a, back_LCH.lab_b])
print("delta_E: ", delta_E_CIE1976(a, b))
print("delta_E_94: ", delta_E_CIE1994(a, b))
print("delta_E_00: ", delta_E_CIE2000(a, b))

#Различие RGB-LAB
print("РАЗЛИЧИЕ RGB-LAB")
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([back_RGB.lab_l, back_RGB.lab_a, back_RGB.lab_b])
print("delta_E: ", delta_E_CIE1976(a, b))
print("delta_E_94: ", delta_E_CIE1994(a, b))
print("delta_E_00: ", delta_E_CIE2000(a, b))

#Различие HSB-LAB
print("РАЗЛИЧИЕ HSB-LAB")
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([back_HSB.lab_l, back_HSB.lab_a, back_HSB.lab_b])
print("delta_E: ", delta_E_CIE1976(a, b))
print("delta_E_94: ", delta_E_CIE1994(a, b))
print("delta_E_00: ", delta_E_CIE2000(a, b))

#Различие HSI-LAB
print("РАЗЛИЧИЕ HSI-LAB")
a = np.array([LAB.lab_l, LAB.lab_a, LAB.lab_b]).astype('float')
b = np.array([back_HSI.lab_l, back_HSI.lab_a, back_HSI.lab_b])
print("delta_E: ", delta_E_CIE1976(a, b))
print("delta_E_94: ", delta_E_CIE1994(a, b))
print("delta_E_00: ", delta_E_CIE2000(a, b))