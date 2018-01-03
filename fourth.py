import cv2

image = cv2.imread('pic.png', -1)

cv2.imshow('Picture', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
