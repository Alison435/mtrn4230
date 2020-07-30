#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import String

#publish pose to publisher nampedpose
def named_pose(pose_name):
	pub = rospy.Publisher('namedpose', String, queue_size = 10)
	rate = rospy.Rate(10)
	rospy.loginfo(pose_name)
	pub.publish(pose_name)


#publish object descriptors to publisher packobject
def pack_object(colour, shape):
	pub = rospy.Publisher('packobject', String, queue_size = 10)
	rate = rospy.Rate(10)
	rospy.loginfo(colour)
	pub.publish(colour)

	rospy.loginfo(shape)
	pub.publish(shape)




if __name__ == '__main__':
    try:
        rospy.init_node("Planner", anonymous=True)	#might no leave this here - initialise node in main?
	print("Initialising planner node")
	
	while True:
		pack_object("red", "square")
		print("function called")
		time.sleep(6)


    except rospy.ROSInterruptException:
	pass




	





