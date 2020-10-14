import cv2
import numpy as np
img=cv2.imread('czl.jpg',1)#图片读取
cv2.imshow('img',img)
#图片缩放
img = cv2.resize(img,None,fx=0.5,fy=0.5)
rows,cols,channels = img.shape
print(rows,cols,channels)
cv2.imshow('img',img)
#图片转为灰度图像
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#图片的二值化处理
lower_blue = np.array([90,70,70])
upper_blue = np.array([110,255,255])
mask = cv2.inRange(hsv,lower_blue,upper_blue)
cv2.imshow('mask',mask)#图片显示

#图像的腐蚀和膨胀
erode=cv2.erode(mask,None,iterations=1)
cv2.imshow('erode',erode)#图片显示

dilate=cv2.dilate(mask,None,iterations=1)
cv2.imshow('dilate',dilate)#图片显示

###


cv2.waitKey(0)
