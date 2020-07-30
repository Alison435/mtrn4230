#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String


def callback(info):
	rospy.loginfo(info.data)
	print "I heard ", info.data

def listen_pose():
	rospy.Subscriber("packobject", String, callback)
	rospy.spin()

if __name__ == '__main__':
    try:
        rospy.init_node("Listen", anonymous=True)	#might no leave this here - initialise node in main?
	print("Initialising listen node")
	
	while True:
		listen_pose()


    except rospy.ROSInterruptException:
	pass




	





