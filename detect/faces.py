import cv2
import numpy as np

# loading haar cascade xml files

classifier = cv2.CascadeClassifier('./haar_cascade/haarcascade_frontalcatface.xml')

image = cv2.imread('testingtarget/family.jpg')

# detectmultiface

for (x1,x2,y1,y2) :

    cv2.rectangle()


cv2.imshow("original",image);
cv2.imshow("after",after)