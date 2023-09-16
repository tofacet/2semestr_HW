from skimage.io import imread, imshow, imsave
from skimage import img_as_float, img_as_ubyte
from numpy import histogram as hist
from numpy import dstack
import numpy as np

import warnings
warnings.filterwarnings("ignore")

global name, ims 

im=[0,0,0]
impr=[0,0,0]

# Параметры
# В папке с программой должны лежать изображения вида 0.jpg, 1.jpg... 99999.jpg
pix = 1             # число картинок в папке для обработки
ext = ('png')       # тип входных файлов 
extout = ('png')    # тип выходных
img_center = 1      # центровка спектра
img_hist = 1        # выравнивание гистрограммы
save_pic = 0        # экспорт отдельной картинки
save_stack = 1      # экспорт склеенной картинки

# Разложение каждого из каналов в спектр,
# на вход функции подается номер канала, имя картинки и необходимость цетровки
def chan(n,img,shift):        
    img = np.fft.fft2(img[:,:,n])
    if shift==True:
        img = np.fft.fftshift(img)    # центровка спектра 
    return img

# Обработка всх каналов картинки
def comp(ims,shift,align):
    im[0] = np.log(1+abs(chan(0,ims,shift)))     # Создание визуализации для каналов
    im[0] = im[0]/im[0].max()                    # Масштабирование яркости
    if align==1:                                 # Выравнивание гистограммы
        imt = img_as_ubyte(im[0])
        iy, ix = imt.shape
        values, bin_edges = hist(imt.ravel(), bins=range(257))
        for k in range(257):
            cdf = np.cumsum(values[:k])
        count = 0
        for m in range(256):
            count += cdf[m]
            if count > 0:
                x_min = 0
                break
        cdfmin = cdf[x_min:].min()    
        imt = np.round( (cdf[imt]-cdfmin)/(iy*ix-1)*255 )
        imt = np.array(imt, dtype=np.uint8)
        im[0] = imt
    return im

for p in range(pix):
    cap = p
    name = str(cap)+'.'+ext
    ims = imread(name)
    if ims.shape[2]>2:
        ims = dstack((ims[:,:,0],ims[:,:,1],ims[:,:,2]))
    
    # Визуализация центрованного спектра: изображение, сдвиг, выравнивание гистграммы
    impr1 = comp(ims,img_center,img_hist)
    
    # Сохранение визуализации спектра
    if save_pic==1:
        imsave('export-'+str(cap)+'.'+extout, impr1)
    
    # Сохранение склеенной картинки и спектра
    if save_stack==1:
        if impr1.shape[0]>=impr1.shape[1]:
            imsave('stack-'+str(cap)+'.'+extout, np.hstack((ims,impr1))) 
        else:
            imsave('stack-'+str(cap)+'.'+extout, np.vstack((ims,impr1)))
    
    #imsave('export-'+str(cap)+'-st2.'+ext, np.hstack((imread(name),'export-'+str(cap)+'.'+extout)))
    
    # Строка состояния
    print("\r",name+' - OK!', end=" ")
    
print(' === COMPLETE ===')