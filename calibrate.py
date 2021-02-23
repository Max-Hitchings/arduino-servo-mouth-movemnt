import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

Smallest = 999
largest = 0
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)
    for face in faces:
        landmarks = predictor(frame, face)
        
        topLip = (landmarks.part(51).x, landmarks.part(51).y)
        bottomLip = (landmarks.part(57).x, landmarks.part(57).y)
        
        distanceBetweenLips = bottomLip[1]-topLip[1]
        if distanceBetweenLips > largest:
            largest = distanceBetweenLips
            print(f"largest: {distanceBetweenLips}")

        if distanceBetweenLips < Smallest:
            Smallest = distanceBetweenLips
            print(f"Smallest: {distanceBetweenLips}")

        cv2.circle(frame, topLip, 3, (255, 0, 0), -1)
        cv2.circle(frame, bottomLip, 3, (255, 0, 0), -1)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
print(f"largest distance: {largest}\nSmallest distance: {Smallest}")