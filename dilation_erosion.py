import cv2
import numpy as np

# import image
img = cv2.imread('neww.jpg')

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)


cv2.imshow('image',erosion)
cv2.imshow('image',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
