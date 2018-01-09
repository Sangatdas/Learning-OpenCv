import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/j.png')
kernel = np.ones((5, 5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# Opening
open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Closing
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Tophat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Blackhat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Frame', gradient)


cv2.waitKey(0)
cv2.destroyAllWindows()