import cv2
import numpy as np

# import image
img = cv2.imread('/home/nalin/Pictures/neww.png')

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow('image',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
