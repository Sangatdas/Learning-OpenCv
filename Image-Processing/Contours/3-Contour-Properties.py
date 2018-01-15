import cv2

img = cv2.imread('../img/india.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Frame', thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()

#
# gray = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
#
# cv2.imshow('india_inv.png', gray)

