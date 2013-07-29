#!/usr/bin/env python
import rosbag
import rospy
from std_msgs.msg import Int32, String

bag = rosbag.Bag('test.bag', 'w')

try:
    str = String()
    str.data = 'foo'

    i = Int32()
    i.data = 42
    pub = rospy.Publisher('/joint_states', String)
    bag.write('/joint_states', pub)
    bag.write('numbers', i)
finally:
    bag.close()
