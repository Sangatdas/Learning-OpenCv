import cv2
import numpy as np

img1 = cv2.imread('img/1.jpg')
img2 = cv2.imread('img/2.jpg')

dst = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
