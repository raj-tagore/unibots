#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def camera_publisher():
    # Initialize the ROS node
    rospy.init_node('camera_publisher', anonymous=True)

    # Create a publisher for the image topic
    image_pub = rospy.Publisher('/image_raw', Image, queue_size=10)

    # Create a CvBridge object
    bridge = CvBridge()

    # Create a VideoCapture object to access the camera
    cap = cv2.VideoCapture(0)

    # Set the camera resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Loop to continuously capture and publish images
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        # Capture frame from the camera
        ret, frame = cap.read()

        if ret:
            # Convert the OpenCV image to a ROS image message
            ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")

            # Publish the ROS image message
            image_pub.publish(ros_image)

        # Sleep to maintain the desired publishing rate
        rate.sleep()

    # Release the camera and destroy any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        camera_publisher()
    except rospy.ROSInterruptException:
        pass