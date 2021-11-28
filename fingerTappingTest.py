import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    

    cv2.imshow('img', img)
    cv2.waitKey(1)
    
    
