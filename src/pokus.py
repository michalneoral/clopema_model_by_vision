#!/usr/bin/env python
"""Functions for work with bag files"""
import roslib; roslib.load_manifest('clopema_smach')
import rospy, smach, smach_ros, math, copy, tf, PyKDL, os, shutil, numpy, time, subprocess
from _bag_files_hydro import stop_bag_file, start_bag_file_camera_def, start_bag_file_topic
from actions import GoHome, GoToAction, ActionMove, OpenGrip, CloseGrip, GoToActionJoints_r1, GoToActionJoints_r2, ExtAxisMove
    
def main():
    rospy.init_node('collect_data')
    ActionMove(0,0)   

if __name__ == '__main__':
    main()
