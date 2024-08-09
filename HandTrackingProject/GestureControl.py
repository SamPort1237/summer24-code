import cvzone
import cv2

cap = cv2.VideoCapture(0)
detector = cvzone.HandDetector(maxHands=1, detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    cv2.imshow('Image', img)
    cv2.waitKey(1)