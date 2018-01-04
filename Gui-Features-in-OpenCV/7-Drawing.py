import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

img = cv2.rectangle(img, (256, 256), (509, 509), (0, 0, 255), 3)

img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

img = cv2.circle(img, (256, 256), 40, (0, 255, 0), 5)

pts = np.array([[10, 5],[20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
img = cv2.polylines(img, [pts], True, (0, 0, 255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Open CV', (0, 500), font, 3, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow('Line', img)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
