import cv2
import numpy as np
import pyrealsense2
from realsense_depth import *


#initialize camera intel realsence
depth_camera = DepthCamera()

ret,depth_frame, color_frame = depth_camera.get_frame()

print(depth_frame)
print(np.array(depth_frame).shape, np.array(color_frame).shape)

cv2.imshow("depth frame", depth_frame)
cv2.imshow("color frame", color_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()