import cv2
import numpy as np

# import image
img = cv2.imread('/home/nalin/Pictures/neww.png')

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


HSV_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
edged = cv2.Canny(gray, 30, 200) 
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)






cv2.waitKey(0)


cv2.imwrite('contours.png',img)
