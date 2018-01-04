import cv2
import numpy as np

img = cv2.imread('img/roi.jpg', 1)

px = img[100, 100]
print px

blue = img[100, 100, 0]
print blue

img[100, 100] = [255, 255, 255]
print img[100, 100]

print img.item(10, 10, 2)

img.itemset((10, 10, 2), 100)
print img.item((10, 10, 2))

print img.shape
box = img[220:280, 390:450]
img[0:60, 0:60] = box

box[:, :, 2] = 0
cv2.imshow('Frame', img)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
