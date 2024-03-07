#!/usr/bin/env python

import rospy
import serial
from std_msgs.msg import String
import time


def callback(data):
    try:
        # Send the data via serial
        ser.write(data.data.encode())
        rospy.loginfo("Data sent: " + str(data.data))
    except serial.SerialException as e:
        rospy.logerr("Serial communication error: " + str(e))

def listener():

    # Wait for 3s after serial port opens
    time.sleep(3)
    # Initialize the ROS node
    rospy.init_node('send_decision', anonymous=True)
    # Subscribe to the topic
    rospy.Subscriber('/decision', String, callback) 
    # Spin until the node is shut down
    rospy.spin()

if __name__ == '__main__':

    # Open the serial port
    ser = serial.Serial('/dev/ttyACM0', 9600) # Replace '/dev/ttyUSB0' with the actual serial port
    listener()
    # Close the serial port when the node is shut down
    rospy.on_shutdown(ser.close)