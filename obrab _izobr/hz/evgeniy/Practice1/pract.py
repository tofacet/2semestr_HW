# 1. pip install colormath - color.math
# 2. pip install --user colour-science
# 3. С версии numpy 1.16.0 метод numpy.asscalar() считается устаревшим, но первая библиотека всё же опирается на него,
# поэтому в файле color_diff.py данной библиотеки (colormath) все строчки вида:
    # return numpy.asscalar(delta_e) следует заменить на новый стандарт вида (ниже):
    # return delta_e.item()

from colormath.color_objects import LabColor, LCHabColor, XYZColor, HSVColor, HSLColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000, delta_e_cmc, delta_e_cie1994
# Значения цвета в LAB задаются через светлоту (Lightness) и две координаты, отвечающие за хроматическую составляющую: тон и насыщенность.
# A — положение цвета в диапазоне от зелёного до красного, B — от синего до жёлтого.
# https://colorizer.org/
_LAB_COLOR = LabColor(88, 45, -70)
_LCH_COLOR = convert_color(_LAB_COLOR, LCHabColor)
_RGB_COLOR = convert_color(_LAB_COLOR, sRGBColor)
_HSB_COLOR = convert_color(_LAB_COLOR, HSVColor) # HSB - пвсевдоним HSV
_HSI_COLOR = convert_color(_LAB_COLOR, HSLColor) # HSI - пвсевдоним HSL
print("LAB: ", _LAB_COLOR)
print("LCH: ", _LCH_COLOR)
print("RGB: ", _RGB_COLOR)
print("HSB: ", _HSB_COLOR)
print("HSI: ", _HSI_COLOR)
print("-----------------------------------------------------")
# Обратное конвертирование в LAB
_LSH_TO_LAB_COLOR = convert_color(_LCH_COLOR, LabColor)
_RGB_TO_LAB_COLOR = convert_color(_RGB_COLOR, LabColor)
_HSB_TO_LAB_COLOR = convert_color(_HSB_COLOR, LabColor)
_HSI_TO_LAB_COLOR = convert_color(_HSI_COLOR, LabColor)
print("LSH->LAB: ", _LSH_TO_LAB_COLOR)
print("RGB->LAB: ", _RGB_TO_LAB_COLOR)
print("HSB->LAB: ", _HSB_TO_LAB_COLOR)
print("HSI->LAB: ", _HSI_TO_LAB_COLOR)
print("*****************************************************")

# Рассчитать ∆E, ∆E_94, ∆E_00
print("Delta LSH->LAB: ", delta_e_cmc(_LAB_COLOR, _LSH_TO_LAB_COLOR))
print("Delta RGB->LAB: ", delta_e_cmc(_LAB_COLOR, _RGB_TO_LAB_COLOR))
print("Delta HSB->LAB: ", delta_e_cmc(_LAB_COLOR, _HSB_TO_LAB_COLOR))
print("Delta HSI->LAB: ", delta_e_cmc(_LAB_COLOR, _HSI_TO_LAB_COLOR))
print("Delta 94 LSH->LAB: ", delta_e_cie1994(_LAB_COLOR, _LSH_TO_LAB_COLOR))
print("Delta 94 RGB->LAB: ", delta_e_cie1994(_LAB_COLOR, _RGB_TO_LAB_COLOR))
print("Delta 94 HSB->LAB: ", delta_e_cie1994(_LAB_COLOR, _HSB_TO_LAB_COLOR))
print("Delta 94 HSI->LAB: ", delta_e_cie1994(_LAB_COLOR, _HSI_TO_LAB_COLOR))
print("Delta 00 LSH->LAB: ", delta_e_cie2000(_LAB_COLOR, _LSH_TO_LAB_COLOR))
print("Delta 00 RGB->LAB: ", delta_e_cie2000(_LAB_COLOR, _RGB_TO_LAB_COLOR))
print("Delta 00 HSB->LAB: ", delta_e_cie2000(_LAB_COLOR, _HSB_TO_LAB_COLOR))
print("Delta 00 HSI->LAB: ", delta_e_cie2000(_LAB_COLOR, _HSI_TO_LAB_COLOR))
print("#####################################################")