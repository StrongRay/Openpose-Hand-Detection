# Openpose-Hand-Detection
CMU Perpetual Computing Lab Openpose modifications to show only Hand detection
Licence:  https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE

Environment for this build:

Ubuntu 18.04  
Python 3.5.3  
OpenCV 4.0.0-alpha  
Openpose 1.4.0 [https://github.com/ortegatron/hand_standalone]

The current openpose version by CMU doesn't have a python wrapper for Hand point detection.  But Ortegatron created his version based on Openpose 1.3.0.  I took Ortegratron's code and merge into 1.4.0 and rebuild openpose. Placed the generated _openpose.so on the openpose home directory

execute the program op-hands-one-ok.py to see hardcoded hands extraction of COCO hand pose

![image](https://github.com/StrongRay/Openpose-Hand-Detection/blob/master/op-hands-one-ok.png)

Interestingly, the COCO Hand model of 21 points is as follows.  The numpy array of left hands can be obtained from the forward_hands function and can be used to calculate the angles of the fingers.  

![image](https://github.com/StrongRay/Openpose-Hand-Detection/blob/master/keypoints_hand.png)

Openpose is not the only method for hand point detection, pure OpenCV has imbedded DNN codes and using the pose_iter_102000.caffemodel, one can do a net.forward to extract out the hand points.  As always, use of a single image is limited.  Once using webcam, the speed of prediction is more important and techniques can be added to increase the accuracy such as greenscreening the background before detection.

![image](https://github.com/StrongRay/Openpose-Hand-Detection/blob/master/opencv-dnn.png)


