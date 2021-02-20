import cv2
import numpy as np
import dlib
import time
import serial

SMALLEST_DIST = 11 
LARGEST_DIST = 44

arduinoData =  serial.Serial('com4',9600)
TOTAL_DIST = 180

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

multiplyier = TOTAL_DIST / (LARGEST_DIST - SMALLEST_DIST)
latestRequest = 0

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)
        
        topLip = (landmarks.part(51).x, landmarks.part(51).y)
        bottomLip = (landmarks.part(57).x, landmarks.part(57).y)
        
        distanceBetweenLips = bottomLip[1]-topLip[1]

        degree = int(((distanceBetweenLips-11)*multiplyier)+20)
        if abs(latestRequest-degree) > 10:
            latestRequest = degree
            if degree > 180:
                degree = 180
            arduinoData.write(str(degree).encode())
            print(f"sent {degree}")

        cv2.circle(gray, topLip, 3, (255, 0, 0), -1)
        cv2.circle(gray, bottomLip, 3, (255, 0, 0), -1)
    

    time.sleep(1)
    cv2.imshow("Frame", gray)

    key = cv2.waitKey(1)
    if key == 27:
        break

arduinoData.write("90".encode())