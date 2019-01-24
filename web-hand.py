#  Openpose 1.4.0  Handpose recognition via webcam
#  Requires OpenCV installed for Python
#  Hardcoded WebCam (0) 

# import sys
import cv2
import argparse
import pyopenpose as op

# Flags
parser = argparse.ArgumentParser()
parser.add_argument("--image_path", default="../../../examples/media/COCO_val2014_000000000192.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
args = parser.parse_known_args()

# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
params["model_folder"] = "../../../models/"
params["net_resolution"] = "160x80"
params["hand"] = True
params["hand_detector"] = 2
params["body_disable"] = True
params["disable_blending"] = True

# Add others in path?
for i in range(0, len(args[1])):
    curr_item = args[1][i]
    if i != len(args[1])-1: next_item = args[1][i+1]
    else: next_item = "1"
    if "--" in curr_item and "--" in next_item:
        key = curr_item.replace('-','')
        if key not in params:  params[key] = "1"
    elif "--" in curr_item and "--" not in next_item:
        key = curr_item.replace('-','')
        if key not in params: params[key] = next_item

# Construct it from system arguments
# Fixed the handRectangles to only 1 person and 1 big rectangle, don't have to keep changing rectangle
handRectangles = [[op.Rectangle(100.0, 150.0, 328.0, 390.0),op.Rectangle(0., 0., 0., 0.)]]

opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

# Process Image
datum = op.Datum()
datum.handRectangles = handRectangles
cam = cv2.VideoCapture(0) # modify here for camera number
while(cv2.waitKey(1) != 27):
    # Get camera frame
    ret, frame = cam.read()
    datum.cvInputData = frame
    opWrapper.emplaceAndPop([datum])
    frame = datum.cvOutputData
    cv2.rectangle(frame, (100,150), (328,390), (0, 255, 0), 1, 1)
    cv2.imshow("Openpose 1.4.0 Webcam", frame) # datum.cvOutputData)
# Always clean up
cam.release()
cv2.destroyAllWindows()
