import cv2
import numpy as np
import mediapipe as mp

def fingertips(idNumber):
    vr = []
    if id == idNumber:
        vr.append(cx)
        vr.append(cy)
        pontos.append(vr)

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    ret, img = cap.read()
    
    imgBGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgBGR)
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            pontos = []
            for id, lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx,cy)
                
                if id == 0 or id ==4 or id == 8:
                    cv2.circle(img, (cx,cy), 10, (0,0,255), cv2.FILLED)
                
                fingertips(0)
                fingertips(4)
                fingertips(8)

                pts = np.array(pontos, np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img, [pts], True, (0,0,255), 3)

            
            # mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)



    cv2.imshow('img', img)
    cv2.waitKey(1)
    
    
