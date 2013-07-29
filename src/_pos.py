#!/usr/bin/env python
"""file of constatns  of position 
that are use in this package
for quicker change and orientation"""

import roslib; roslib.load_manifest('clopema_smach')
import rospy, smach, smach_ros, math, copy, tf, PyKDL, os, shutil, numpy
from tf.transformations import quaternion_from_euler, quaternion_about_axis, quaternion_from_matrix, rotation_matrix
from tf_conversions import posemath
from clopema_smach import *
from geometry_msgs.msg import *
from smach import State
from clopema_planning_actions.msg import MA1400JointState
from clopema_smach.utility_states import PoseBufferState

#adjustment
visualize = False

#position of x1_xtion
x_pos_r1_xtion = -0.6
y_pos_r1_xtion = -0.6
z_pos_r1_xtion = 1.2
phi_r1_xtion = math.pi
teta_r1_xtion = -math.pi/2
sigma_r1_xtion = -math.pi/4

#first position of r2_ee
x1_pos_r2_ee = 0.35
y1_pos_r2_ee = -1.45
z1_pos_r2_ee = 1.8
phi1_r2_ee = 5*math.pi/8
teta1_r2_ee = math.pi/4
sigma1_r2_ee = 0

#second position of r2_ee
x2_pos_r2_ee = 0.25
y2_pos_r2_ee = -1.55
z2_pos_r2_ee = z1_pos_r2_ee
phi2_r2_ee = phi1_r2_ee
teta2_r2_ee = teta1_r2_ee
sigma2_r2_ee = sigma1_r2_ee

def get_new_pose(x,y,z,phi,teta,sigma):
    """return new position"""
    pose = PoseStamped()
    pose.header.frame_id = 'base_link'
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = z
    pose.pose.orientation = Quaternion(*quaternion_from_euler(phi,teta,sigma))
    return pose

def get_pos_r1_xtion():
    """return position of r1_xtion"""
    return get_new_pose( x_pos_r1_xtion, y_pos_r1_xtion, z_pos_r1_xtion, phi_r1_xtion, teta_r1_xtion, sigma_r1_xtion)
    
def get_pos1_r2_ee():
    """return first position of r2_ee"""
    return get_new_pose( x1_pos_r2_ee, y1_pos_r2_ee, z1_pos_r2_ee, phi1_r2_ee, teta1_r2_ee, sigma1_r2_ee)

def get_pos2_r2_ee():
    """return second position of r2_ee"""
    return get_new_pose( x2_pos_r2_ee, y2_pos_r2_ee, z2_pos_r2_ee, phi2_r2_ee, teta2_r2_ee, sigma2_r2_ee)

def get_poses():
    pose = Pose()
    pose.position.x = x2_pos_r2_ee
    pose.position.y = y2_pos_r2_ee
    pose.position.z = z2_pos_r2_ee
    pose.orientation = Quaternion(*quaternion_from_euler(phi2_r2_ee,teta2_r2_ee,sigma2_r2_ee))

    poses = []
    poses.append(copy.deepcopy(pose))
    pose.position.x = x1_pos_r2_ee
    pose.position.y = y1_pos_r2_ee
    pose.position.z = z1_pos_r2_ee
    pose.orientation = Quaternion(*quaternion_from_euler(phi1_r2_ee,teta1_r2_ee,sigma1_r2_ee))
    poses.append(copy.deepcopy(pose))
    return poses   
   
