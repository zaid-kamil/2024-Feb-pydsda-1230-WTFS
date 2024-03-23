# pre-requisite for this: 
# pip install opencv-contrib-python mediapipe
# run above code in terminal

import cv2
import numpy as np

# for normal laptop with webcam use below
cam = cv2.VideoCapture(0) # 0 is the default camera
# for driodcam use below
# cam = cv2.VideoCapture('http://198.162.1.129:4747/mjpegfeed?640x480')
while cam.isOpened():
    status, frame = cam.read()
    if not status:
        print("⚠️ Camera not available")
        break
    # display output
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) == ord('q'):
        cam.release()
        cv2.destroyAllWindows()
        break