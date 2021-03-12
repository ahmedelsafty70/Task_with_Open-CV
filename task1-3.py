import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    edges = cv2.Canny(frame ,100 ,100)

    cv2.imshow('original',frame)
    cv2.imshow('Sobely',edges)


    k = cv2.waitKey(5) & 0XFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()   
