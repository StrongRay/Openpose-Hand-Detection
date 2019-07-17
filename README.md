# Openpose-Hand-Detection
CMU Perpetual Computing Lab Openpose modifications for v1.4.0 to add Python wrapper for Hand point detection

Licence:  https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE  

Environment for this build:

Ubuntu 18.04  
Python 3.5.3  
OpenCV 4.0.0-alpha  
Openpose 1.4.0 [https://github.com/ortegatron/hand_standalone]

The current openpose version by CMU doesn't have a python wrapper for Hand point detection.  Ortegatron created a nice version but based on Openpose v1.3.0.  I took Ortegratron's code and merge into 1.4.0 and rebuild openpose. Placed the generated _openpose.so on the openpose home directory

execute the program op-hands-one-ok.py to see hard coded hands extraction of COCO hand pose

![image](https://github.com/StrongRay/Openpose-Hand-Detection/blob/master/op-hands-one-ok.png)

COCO Hand model has 21 points as shown below.  The left hands numpy array returned from the forward_hands function can be used to calculate the angles of the fingers for certain recognition of finger gestures.  

![image](https://github.com/StrongRay/Openpose-Hand-Detection/blob/master/keypoints_hand.png)

Openpose is not the only method for hand fingers detection, pure OpenCV has imbedded DNN codes [cv2.dnn.blobFromImage] from v3.4 onwards and download pose_iter_102000.caffemodel weights file, one can do a net.forward to extract out the hand points.  As always, the use of a single image is limited in application.   Using a webcam will allow a stream of hands and the speed of prediction will be more important and techniques can be added to increase the accuracy such as greenscreening the background before detection and python multithreading/processing. 

![image](https://github.com/StrongRay/Openpose-Hand-Detection/blob/master/opencv-dnn.png)

Openpose released a new python wrapper.  I updated the sample code with a webcam viewer https://github.com/StrongRay/Openpose-Hand-Detection/blob/master/web-hand.py
Here's how the hands are detected with a hardcoded handRectangle.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=2t0ppBiyeos" target="_blank"><img src="https://img.youtube.com/vi/2t0ppBiyeos/0.jpg" alt="webcam sample capture" width="240" height="180" border="10" /></a>

Latest Deep Dive into fingers

An interesting exploration into fingers. Extraction seemed to be orientated wrongly. Discovered that lighting makes alot of difference to the detection of fingers. Will move next into finger-straightness-with-tolerance next. 

<a href="http://www.youtube.com/watch?feature=player_embedded&v=xZCUjNnzPrg" target="_blank"><img src="https://img.youtube.com/vi/xZCUjNnzPrg/0.jpg" alt="webcam sample capture" width="240" height="180" border="10" /></a>

Upgraded from UBUNTU 16 to 17 and rebuild OpenCV 4.1 and recompile Openpose 1.5
Look at the speed now

<a href="http://www.youtube.com/watch?feature=player_embedded&v=zYDkhRiaSf8" target="_blank"><img src="https://img.youtube.com/vi/zYDkhRiaSf8/0.jpg" alt="webcam sample capture" width="480" height="320" border="10" /></a>

