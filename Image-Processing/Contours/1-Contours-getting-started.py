import cv2
import numpy as np
import matplotlib.pyplot as plt


# Finding contours
img = cv2.imread('../img/roi.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Drawing contours
img = cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
