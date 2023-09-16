import os, scipy, cv2, numpy as np
for i in os.listdir():
    if not i.endswith('.py'):
        image = cv2.imread(i)
        image = scipy.ndimage.uniform_filter(image, size=(2, 2, 1)) * (1 - (np.random.random(size = image.shape)/10))
        cv2.imwrite(i+'_.jpeg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 10])