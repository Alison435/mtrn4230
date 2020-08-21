#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import json


def callback(info):										#function triggered when message is received
	#rospy.loginfo(info.data)									
	object_info = json.loads(info.data)
	#print temp['cube']['Blue']							#for testing

def listen_pose():
	rospy.Subscriber("ObjectInfo", String, callback)	#subscribe to topic object info

if __name__ == '__main__':
    try:
        rospy.init_node("Listen", anonymous=True)		#planner node already created so no need for this line
	print("Initialising listen node")
	
	while True:
		listen_pose()


    except rospy.ROSInterruptException:
	pass




	





