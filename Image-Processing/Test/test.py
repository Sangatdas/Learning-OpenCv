import cv2
import numpy as np

select = True
coloring = False
mode = True
ix, iy = -1, -1
img = cv2.imread('ferrari.png')

# print img.shape


def myfun(event, x, y, flags, param):

    global ix, iy, mode, img

    global color1

    if event == cv2.EVENT_LBUTTONDOWN:
            ix = x
            iy = y
            color1 = img[iy, ix]
            floodfill(ix, iy)


img[:100, :100] = [0, 255, 0]


def floodfill(x, y):

    b1, g1, r1 = img[y, x]
    b2, g2, r2 = color1

    if r1 != r2:
        img[y, x] = [0, 255, 0]
        floodfill(x + 1, y)
        floodfill(x + 1, y + 1)
        floodfill(x - 1, y + 1)
        floodfill(x - 1, y - 1)

    else:
        return None


cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', myfun)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

