#!/usr/bin/env python
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy as np
import cv2
import cv2.aruco as aruco
import math
from std_msgs.msg import Float32
from sensor_msgs.msg import CompressedImage

index = 1

def convert_color_image(ros_image):
    global index
    bridge = CvBridge()
    try:
        color_image = bridge.imgmsg_to_cv2(ros_image, "bgr8")
        path = "/home/chungyu/test_ws/src/bag_to_video/images/"
        str_index = str(index)
        image_name = path + str_index + ".png"
        cv2.imwrite(image_name, color_image)
        index = index + 1
        
    except CvBridgeError as e:
        print(e)

def bag_to_video():
    rospy.init_node("bag_to_video", anonymous=True)
    rospy.Subscriber("/raw_image", Image, callback=convert_color_image, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        bag_to_video()
    except rospy.ROSInterruptException:
        pass