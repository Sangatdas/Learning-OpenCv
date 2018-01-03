import cv2
import numpy as np

drawing = False
mode = True
ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 0), -1)
            else:
                r = abs(x-ix)
                cv2.circle(img, (ix, iy), r, (255, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 0), -1)
        else:
            r = abs(x-ix)
            cv2.circle(img, (ix, iy), r, (255, 255, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', draw_circle)

while True:
    cv2.imshow('Frame', img)
    k = cv2.waitKey(10) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()