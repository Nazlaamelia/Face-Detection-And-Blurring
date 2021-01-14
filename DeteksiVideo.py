import cv2
import numpy as np
def resize(img,new_width=500):
    height,width,_ = img.shape
    ratio = height/width
    new_height = int(ratio*new_width)
    return cv2.resize(img,(new_width,new_height))

face_cascade = cv2.CascadeClassifier("face_detector.xml")

cap = cv2.VideoCapture("VideoGrup.MOV") 

while True:
    _,frame = cap.read()
    frame = resize(frame)
    detections = face_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=6)

    for face in detections:
        x,y,w,h = face

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Hasil Deteksi Video",frame)
        if cv2.waitKey(1) == 27:
            break

cap.release()
cv2.destroyAllWindows()








    