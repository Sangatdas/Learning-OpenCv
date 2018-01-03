import cv2
import numpy as np


def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 100, (255, 255, 0), 1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', draw_circle)

while True:
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
