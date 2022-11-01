import cv2
import numpy as np

# setting
color = (0,0,255)

color2 = (255,0,255)

# loading haar cascade xml files

classifier = cv2.CascadeClassifier('./haar_cascade/haarcascade_frontalcatface.xml')

image = cv2.imread('testingtarget/family.jpg')

#scenario 1: recognize people face
#process involved: face detection
#using function:

for (x,y,width,height) in image :

    cv2.rectangle(image,(x,y),(x+width,y+height),color2,)

# detectmultiface
checkmultiface = classifier.detectMultiScale()
# name the window

cv2.imshow("original",image)
cv2.imshow("after",after)

#scenario 2:
#process involved:
#using function: 
#description: