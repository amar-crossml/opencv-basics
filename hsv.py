import cv2
import numpy as np

# import image
img = cv2.imread('/home/nalin/Pictures/neww.png')

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('image',HSV_img )
cv2.waitKey(0)
cv2.destroyAllWindows()
