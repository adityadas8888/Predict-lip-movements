<h3><b>Project Title:</b></h3>Prediction of real time speech from lip and jaw movements.
<h4>Project Summary:</h4>
The goal of the project is to predict the words spoken by a particular subject by analyzing the lip and jaw
movements. The subject is expected to speak a single language. The program is expected to predict the
words
spoken as close to real time as possible and preferably in sentences.
<br>
Team Members:<br>
•Aditya Das – 1001675762<br>
•Naman Jain Vimal Kumar – 1001670153
<br>
<img src="https://github.com/adityadas8888/Predict-lip-movements/blob/master/images/flow.png"
<b>Project Work Flow explanation:</b>
1. We are working on a Kinect 360 for this project. The idea is to first get the
video feed and the depth data from the Kinect Camera.
2. Then after taking in the video feed, we are segmenting and detecting the
face.
3. The features of the face are detected using the inbuilt ‘dlib’ library. We are
currently just getting the coordinates of the lips.
4. The future plans are to calibrate the camera and do the feature detection on
a Kinect 360.
 <br>
<b>Future Project Work Flow explanation:</b>
1. We are currently facing issues connecting the Kinect’s ‘OpenNi’ library,
‘primesense’ and ‘libfreenect’ to the OpenCV codebase. But it seems to be a
trivial issue and most probably will be solved soon.
2. The next plans are to train a Neural Model on videos with transcript or
webcam recordings with a dictionary to train the Neural Model on reading
lips.
 <br>
Note:
•Attached videos with the repo showing the project’s progress.
<br>
References:

•https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/<br>
•https://github.com/sachinsdate/lip-movement-net<br>
•https://towardsdatascience.com/face-detection-for-beginners-<br>
e58e8f21aad9
