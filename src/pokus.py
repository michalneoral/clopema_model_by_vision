#!/usr/bin/env python
import roslib; roslib.load_manifest('clopema_smach')
import rospy, smach, smach_ros, math, copy, tf, PyKDL, os, shutil, numpy
from tf.transformations import quaternion_from_euler, quaternion_about_axis
from tf_conversions import posemath
from clopema_smach import *
from geometry_msgs.msg import *
from smach import State
from clopema_planning_actions.msg import MA1400JointState
from clopema_smach.utility_states import PoseBufferState
import _pos
import time

import actions

def main():
    rospy.init_node('shake_it_demo')
    #
    actions.GoToActionJoints_r1(0)
    actions.GoToActionJoints_r2(2,1)
    actions.ActionMove(2,1)


       
if __name__ == '__main__':
    main()
