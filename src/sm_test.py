#!/usr/bin/env python
import roslib; roslib.load_manifest('clopema_smach')
import rospy, smach, smach_ros, math, copy, tf, PyKDL, os, shutil, numpy
from tf.transformations import quaternion_from_euler, quaternion_about_axis
from tf_conversions import posemath
from clopema_smach import *
from clopema_motoros.srv import *
from geometry_msgs.msg import *
from smach import State, Sequence
from clopema_smach.msg import MA1400JointState
from clopema_smach.utility_states import PoseBufferState
from sensor_msgs.msg import JointState
import _pos

def main():
    try:
        print "open"
        f = open("/home/neosh/ros_catkin_ws/src/clopema_model_by_vision/matlab/topics.txt", "r")
        try:
            lines = f.readlines()            
        finally:
            f.close()
    except IOError:
        print lines
        pass
       
if __name__ == '__main__':
    main()
