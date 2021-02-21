import cv2
import numpy as np
import dlib
import time
import serial
import math
#from numToByteDict import numToByteDict

SMALLEST_DIST = 7
LARGEST_DIST = 33

arduinoData =  serial.Serial('com7',9600)
TOTAL_DIST = 180
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
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)
    for face in faces:
        landmarks = predictor(frame, face)
        
        for i in range(0,68):
            x = landmarks.part(i).x
            y = landmarks.part(i).y
            cv2.circle(frame, (x,y), 3, (255, 0, 0), -1)
        
        #cv2.circle(frame, landmarks.part(51).x, 3, (255, 0, 0), -1)
        #cv2.circle(frame, bottomLip, 3, (255, 0, 0), -1)
    

    #time.sleep(1)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

arduinoData.write("90".encode())