#!/usr/bin/env python

#from threading import Timer
#import time
#from _bag_files import start_bag_file_all, stop_bag_file

#pid=start_bag_file_all('Nohavice', 123)
#time.sleep(2)
#stop_bag_file(pid)

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
import _pos, actions

def main():
    rospy.init_node('sm_test')
    
    actions.ActionLinearMove()

if __name__ == '__main__':
    main()
