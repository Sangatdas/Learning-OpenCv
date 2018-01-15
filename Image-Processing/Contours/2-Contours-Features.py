import cv2
import numpy as np

img = cv2.imread('../img/roi.jpg', 0)
ret, thresh = cv2.threshold(img, 60, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]

# Moments
M = cv2.moments(contours[0])
cx = int(M["m10"]/M["m00"])
cy = int(M["m01"]/M["m00"])

# print cx
# print cy

# Area
area = cv2.contourArea(cnt)
print area

# Perimeter
perimeter = cv2.arcLength(cnt, True)
print perimeter

# Approximation
epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)



cv2.waitKey(0)
cv2.destroyAllWindows()
