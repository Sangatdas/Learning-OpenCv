import cv2

image = cv2.imread('img/pic.png', 0)

cv2.imshow('Picture', image)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('image.png', image)
    cv2.destroyAllWindows()
