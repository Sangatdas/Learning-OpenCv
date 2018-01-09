import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/roi.jpg')

G = img.copy()

pics = [G]

for i in xrange(4):
    x = cv2.pyrDown(img)
    pics.append(x)
    img = x

for i in xrange(4):
    plt.subplot(2, 2, i+1), plt.imshow(cv2.Canny(pics[i], 200, 200)), plt.xticks(), plt.yticks()

plt.show()

for i in xrange(4):
    plt.subplot(2, 2, i+1), plt.imshow(cv2.Canny(cv2.pyrUp(pics[i]), 200, 200)), plt.xticks(), plt.yticks()

plt.show()

