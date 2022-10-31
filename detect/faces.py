import cv2
import numpy as np

# loading haar cascade xml files

image = cv2.CascadeClassifier('./haar_cascade/haarcascade_frontalcatface.xml')