import cv2
import numpy as np
import dlib
import time
import serial
import math
#from numToByteDict import numToByteDict

SMALLEST_DIST = 13
LARGEST_DIST = 50

arduinoData =  serial.Serial('com7',9600)
TOTAL_DIST = 160
numToByteDict = {
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
    16: "g",
    17: "h",
    18: "i"
}

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

multiplyier = TOTAL_DIST / (LARGEST_DIST - SMALLEST_DIST)
latestRequest = 0

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)
    for face in faces:
        landmarks = predictor(frame, face)
        
        topLip = (landmarks.part(51).x, landmarks.part(51).y)
        bottomLip = (landmarks.part(57).x, landmarks.part(57).y)
        
        distanceBetweenLips = bottomLip[1]-topLip[1]

        degree = int(((distanceBetweenLips-SMALLEST_DIST)*multiplyier)+20)
        if abs(latestRequest-degree) > 10:
            latestRequest = degree
            if degree > 180:
                degree = 180
            degree = int((round(degree, -1))/10)
            if degree<=9:
                arduinoData.write(str(degree).encode())
                print(f"sent {degree}")
            else:
                arduinoData.write(numToByteDict[degree].encode())
                print(f"sent {numToByteDict[degree]}, {degree} ")

        cv2.circle(frame, topLip, 3, (255, 0, 0), -1)
        cv2.circle(frame, bottomLip, 3, (255, 0, 0), -1)
    

    #time.sleep(1)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

arduinoData.write("9".encode())