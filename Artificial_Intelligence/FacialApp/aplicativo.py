import cv2 
from cvzone.FaceDetectionModule import FaceDetector

video = cv2.VideoCapture(0)

detector = FaceDetector()

while True: 
    _,img = video.read()
    img,bboxes = detector.findFaces(img,draw=True)

    cv2.imshow('Resultado', img)
    if cv2.waitKey(1) ==27:
        break