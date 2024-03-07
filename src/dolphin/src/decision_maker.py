#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def publish_string():
    # Initialize the ROS node
    rospy.init_node('decision_maker', anonymous=True)
    # Create a publisher for the topic
    pub = rospy.Publisher('/decision', String, queue_size=1)
    # Set the publishing rate (in Hz)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # Create a string message
        message = "1"
        # Publish the message
        pub.publish(message)
        # Sleep to maintain the publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_string()
    except rospy.ROSInterruptException:
        pass