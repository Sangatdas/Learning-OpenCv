import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/roi.jpg', 0)

edges = cv2.Canny(img, 200, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.yticks([]), plt.yticks([])

plt.show()
