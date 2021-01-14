import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("face_detector.xml")

img = cv2.imread("rame.jpeg")

detections = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)

for face in detections :
        x,y,w,h = face 
        
        img[y:y+h,x:x+w] = cv2.GaussianBlur(img[y:y+h,x:x+w],(15,15),cv2.BORDER_DEFAULT)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Hasil Blur Wajah", img)

cv2.waitKey(0)


