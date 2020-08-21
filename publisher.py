#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import json


def talker():
    pub = rospy.Publisher("ObjectInfo", String, queue_size = 10)
    json_str = {"rectangle": {"Red" : 1, "Green": 2, "Blue": 0 },"cube": { "Red" : 1, "Green":0, "Blue": 4}}    #harcoding values
    object_info = json.dumps(json_str)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo(object_info)
        pub.publish(object_info)
        rate.sleep()


if __name__ == '__main__':
    try:
        rospy.init_node("planner", anonymous=True)		#planner node already created so no need for this line
        print("Initialising publisher  node")
        talker()


    except rospy.ROSInterruptException:
	pass
