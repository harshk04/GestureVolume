
import cv2
import numpy as np
import HandTrackingModule as htm
import time

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)

cap. set (3, wCam) 
cap.set (4, hCam)
pTime=0


detector = htm.handDetector(detectionCon=0.9)


while(True):
	
	# Capture frames in the video
	success, frame = cap.read()
	frame = detector.findHands(frame)
	lmList = detector.findPosition(frame)

	if len(lmList) != 0:
		print(lmList[4], lmList[8])
	
	# x1, y1 = lmList[4][1], lmList[4][2]
	# x2, y2 = lmList[8][1], lmList[8][2]
	# cv2.circle(frame, (x1, y1), 15, (255, 0, 255), cv2. FILLED) 
	# cv2.circle(frame, (x2, y2), 15, (255, 0, 255), cv2. FILLED)
	# cv2.line (frame, (x1, y1), (×2, y2), (255, 0, 255), 3)

	cTime = time.time ()
	fps = 1 / (cTime - pTime)
	pTime = cTime

	
	font = cv2.FONT_HERSHEY_SIMPLEX       # describe the type of font to be used.

	
	cv2.putText(frame,f'FPS: {int(fps)}',(10, 50),	font, 1,(0, 0, 255),2,cv2.LINE_4)     # Use putText() method for
	

	
	cv2.imshow('video', frame)      # Display the resulting frame

	# creating 'q' as the quit
	# button for the video
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release the cap object
cap.release()
# close all windows
cv2.destroyAllWindows()
