import cv2

image = cv2.imread('img/pic.png', -1)
cv2.namedWindow("Picture", cv2.WINDOW_NORMAL)
cv2.imshow('Picture', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
