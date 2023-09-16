# 1. pip install colormath - color.math
# 2. pip install --user colour-science
# 3. С версии numpy 1.16.0 метод numpy.asscalar() считается устаревшим, но первая библиотека всё же опирается на него,
# поэтому в файле color_diff.py данной библиотеки (colormath) все строчки вида:
    # return numpy.asscalar(delta_e) следует заменить на новый стандарт вида (ниже):
    # return delta_e.item()

from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000, delta_e_cmc, delta_e_cie1994
from colormath.color_objects import LabColor, LCHabColor as LCH_LIB, HSVColor as HSB_LIB, HSLColor as HSI_LIB, sRGBColor as RGB_LIB
# LAB = 
# Lightness - свет
# A - положение цвета от зелёного до красного
# B - положение цвета от синего до жёлтого

LAB = LabColor(52, 46, 60)
LCH = convert_color(LAB, LCH_LIB)
RGB = convert_color(LAB, RGB_LIB)
HSB = convert_color(LAB, HSB_LIB)
HSI = convert_color(LAB, HSI_LIB)

# Цвет в заданных форматах
print("LAB: ", LAB)
print("LCH: ", LCH)
print("RGB: ", RGB)
print("HSB: ", HSB)
print("HSI: ", HSI, "\n")

# Обратное конвертирование в LAB
FROM_LCH_TO_LAB = convert_color(LCH, LabColor)
FROM_RGB_TO_LAB = convert_color(RGB, LabColor)
FROM_HSB_TO_LAB = convert_color(HSB, LabColor)
FROM_HSI_TO_LAB = convert_color(HSI, LabColor)

print("LCH to LAB: ", FROM_LCH_TO_LAB)
print("RGB to LAB: ", FROM_RGB_TO_LAB)
print("HSB to LAB: ", FROM_HSB_TO_LAB)
print("HSI to LAB: ", FROM_HSI_TO_LAB, "\n")

# ∆E, ∆E_94, ∆E_00
print("Delta LCH to LAB: ", delta_e_cmc(LAB, FROM_LCH_TO_LAB))
print("Delta RGB to LAB: ", delta_e_cmc(LAB, FROM_RGB_TO_LAB))
print("Delta HSB to LAB: ", delta_e_cmc(LAB, FROM_HSB_TO_LAB))
print("Delta HSI to LAB: ", delta_e_cmc(LAB, FROM_HSI_TO_LAB), "\n")

print("Delta 94 LCH to LAB: ", delta_e_cie1994(LAB, FROM_LCH_TO_LAB))
print("Delta 94 RGB to LAB: ", delta_e_cie1994(LAB, FROM_RGB_TO_LAB))
print("Delta 94 HSB to LAB: ", delta_e_cie1994(LAB, FROM_HSB_TO_LAB))
print("Delta 94 HSI to LAB: ", delta_e_cie1994(LAB, FROM_HSI_TO_LAB), "\n")

print("Delta 00 LCH to LAB: ", delta_e_cie2000(LAB, FROM_LCH_TO_LAB))
print("Delta 00 RGB to LAB: ", delta_e_cie2000(LAB, FROM_RGB_TO_LAB))
print("Delta 00 HSB to LAB: ", delta_e_cie2000(LAB, FROM_HSB_TO_LAB))
print("Delta 00 HSI to LAB: ", delta_e_cie2000(LAB, FROM_HSI_TO_LAB))