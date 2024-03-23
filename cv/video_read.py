import cv2
import numpy as np
path = r'C:\Users\ZAID\Videos\jjk.mp4'
cam = cv2.VideoCapture(path)
while cam.isOpened():
    status, frame = cam.read()
    if not status:
        print("⚠️ Video frame not frame")
        continue
    cv2.imshow("webcam", frame)
    if cv2.waitKey(3) == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break