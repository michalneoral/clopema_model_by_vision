#!/usr/bin/env python
import roslib; roslib.load_manifest('clopema_smach')
import rospy, smach, smach_ros, math, copy, tf, PyKDL, os, shutil, numpy
from tf.transformations import quaternion_from_euler, quaternion_about_axis, quaternion_from_matrix, rotation_matrix
from tf_conversions import posemath
from clopema_smach import *
from geometry_msgs.msg import *
from smach import State
from clopema_planning_actions.msg import MA1400JointState
import _pos, actions
from _bag_files import start_bag_file_all, stop_bag_file, last_name, delete_last

def main():
    rospy.init_node('sm_test')

    last_name()

if __name__ == '__main__':
    main()
