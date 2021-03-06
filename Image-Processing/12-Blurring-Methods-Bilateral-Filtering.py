import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/opencv.png')

blur = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Bilateral Filtering')
plt.xticks([]), plt.yticks([])
plt.show()
