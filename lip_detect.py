# python3 lip_detect.py --shape-predictor shape_predictor_68_face_landmarks.dat
# python3 lip_detect.py --shape-predictor shape_predictor_68_face_landmarks.dat --picamera 1


from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
temp = ['python3', 'lip_detect.py', '--shape-predictor', 'shape_predictor_68_face_landmarks.dat']
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-r", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())
#print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
#print("[INFO] camera sensor warming up...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=600)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 0)

	for rect in rects:
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		lips = shape[lStart:lEnd]
		liphull = cv2.convexHull(lips)
		#cv2.drawContours(frame, [liphull], -1, (0, 255, 0), 1)
		for (x, y) in lips:
			cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
			print(x,y)
	  
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	if key == ord("q"):
		break
 
cv2.destroyAllWindows()
vs.stop()