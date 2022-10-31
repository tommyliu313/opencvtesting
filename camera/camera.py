import numpy as np
import cv2

# screen size
screen_width_proportion = 0.5
screen_height_proportion = 0.5
coordinates = (0,0)

cap = cv2.VideoCapture(0)

while(True):
     ret, frame = cap.read()
     frame = cv2.resize(frame, coordinates, fx=screen_width_proportion, fy=screen_height_proportion)
     cv2.imshow('frame',frame)
     ch = cv2.waitKey(1)
     if ch & 0xFF == ord('e'):
	     break

cap.release()
cv2.destroyAllWindows()