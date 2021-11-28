import cv2
import numpy as np
import mediapipe as mp


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    ret, img = cap.read()
    
    imgBGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgBGR)
    print(results.multi_hand_landmarks)


    cv2.imshow('img', img)
    cv2.waitKey(1)
    
    
