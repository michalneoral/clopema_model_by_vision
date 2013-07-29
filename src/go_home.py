#!/usr/bin/env python
import roslib; roslib.load_manifest('clopema_smach')
import rospy, smach, smach_ros, math, copy, tf, PyKDL, os, shutil, numpy
import actions

def main():
    node='go_home'
    rospy.init_node(node)

    actions.GoHome(node)    

if __name__ == '__main__':
    main()
