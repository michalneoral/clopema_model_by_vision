#!/usr/bin/env python
import roslib; roslib.load_manifest('beginner_tutorials')
import rospy
import rosbag
from sensor_msgs.msg import *

bag = rosbag.Bag('test2.bag', 'w')

def callback(data):
    #rospy.loginfo(rospy.get_name() + ": I heard %s" % data.name[1])
    print data
    try:		
        bag.write('/joint_states', data.message)
    finally:
        bag.close()

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

