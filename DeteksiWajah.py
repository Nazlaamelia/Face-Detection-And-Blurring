import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("face_detector.xml")

#Untuk memasukkan file
img = cv2.imread("kelompok.jpeg")

detections = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)

for face in detections :
        x,y,w,h = face 

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Hasil Deteksi Wajah", img)

cv2.waitKey(0)