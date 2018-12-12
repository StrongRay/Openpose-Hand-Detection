import numpy as np
import cv2
import sys
import os
import openpose as op

params = dict()
params["logging_level"] = 3
params["output_resolution"] = "-1x-1"
params["net_resolution"] = "-1x368"
params["model_pose"] = "BODY_25"
params["alpha_pose"] = 0.6
params["scale_gap"] = 0.3
params["scale_number"] = 1
params["render_threshold"] = 0.05
params["num_gpu_start"] = 0
params["disable_blending"] = False
params["default_model_folder"] = "/home/kenghee/openpose/models/"

openpose = op.OpenPose(params)

frame = cv2.imread("/home/kenghee/openpose/examples/media/h5.jpg")

# one person, only one left hand
hands_rectangles = [[[200, 150, 428, 390], [0, 0, 0, 0]]]

for box in hands_rectangles[0]:
    cv2.rectangle(frame, (box[0],box[1]), (box[2],box[3]), (77, 255, 9), 3, 1)

left_hands, right_hands,frame = openpose.forward_hands(frame, hands_rectangles, True)

print ("left hands:")
print (left_hands)

while 1:
    cv2.imshow("output", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
