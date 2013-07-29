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

def OpenGrip(name = 'open_grip', _open=True):
    sm = gensm_grippers(False, _open)
    sm.execute()

def CloseGrip(name = 'close_grip'):
	OpenGrip(_open=False)

def _move(name, new_smash, new_smash_plan):
    with new_smash:
        smach.Sequence.add('GOTO', new_smash_plan, transitions={'aborted':'POWER_OFF'})
        smach.Sequence.add('POWER_OFF', SetServoPowerOffState())

    sis = smach_ros.IntrospectionServer(name, new_smash, '/SM_ROOT')
    sis.start()
    #os.system('clear')
    outcome = new_smash.execute()
    sis.stop()
    
def GoHome(name = 'go_home'):
    new_smash = smach.Sequence(outcomes=['succeeded', 'preempted', 'aborted'], connector_outcome='succeeded')
    new_smash_plan = gensm_plan_vis_exec(PlanToHomeState(), input_keys=[], output_keys=[], visualize = _pos.visualize)
    _move(name, new_smash, new_smash_plan)
    
def GoToAction(name = 'go_actions'):
    new_smash = smach.Sequence(outcomes=['succeeded', 'preempted', 'aborted'], connector_outcome='succeeded')
    new_smash_plan = gensm_plan_vis_exec(Plan1ToXtionPoseState(), input_keys=['goal', 'ik_link'], output_keys=[], visualize = _pos.visualize)
    new_smash.userdata.goal = _pos.get_pos_r1_xtion()
    new_smash.userdata.ik_link = 'r1_xtion'
    _move(name, new_smash, new_smash_plan)    

    new_smash = smach.Sequence(outcomes=['succeeded', 'preempted', 'aborted'], connector_outcome='succeeded')
    new_smash_plan = gensm_plan_vis_exec(Plan1ToPoseState(), input_keys=['goal', 'ik_link'], output_keys=[], visualize = _pos.visualize)
    new_smash.userdata.goal = _pos.get_pos1_r2_ee()
    new_smash.userdata.ik_link = 'r2_ee'
    _move(name, new_smash, new_smash_plan)
    
    OpenGrip()

def ActionMove(name = 'move_measure'):
    poses = _pos.get_poses()

    sm = smach.Sequence(outcomes=['succeeded', 'preempted', 'aborted'], connector_outcome='succeeded')
    sm_plan = gensm_plan_vis_exec(Plan1ToPoseState(), input_keys=['goal', 'ik_link'], output_keys=[], visualize = _pos.visualize)
    sm.userdata.poses = PoseArray()
    sm.userdata.poses.header.frame_id = 'base_link'
    sm.userdata.poses.poses = poses
    sm.userdata.ik_link = 'r2_ee' 
    
    with sm:
        smach.Sequence.add('POSE_BUFFER', PoseBufferState(), transitions={'aborted':'POWER_OFF'})
        smach.Sequence.add('GOTO', sm_plan, transitions={'aborted':'POSE_BUFFER', 'succeeded':'POSE_BUFFER'},
                           remapping={'goal':'pose'})
        smach.Sequence.add('POWER_OFF', SetServoPowerOffState())

    sis = smach_ros.IntrospectionServer(name, sm, '/SM_ROOT')
    sis.start()
    #os.system('clear')
    outcome = sm.execute()
    sis.stop()

#def ActionLinearMove(name = 'move_measure'):
    #poses = []
    #poses.append(copy.deepcopy(_pos.get_pos2_r2_ee))
    #poses.append(copy.deepcopy(_pos.get_pos1_r2_ee))

    #sm = smach.Sequence(outcomes=['succeeded', 'preempted', 'aborted'], connector_outcome='succeeded')
    #sm_plan = gensm_plan_vis_exec(Interpolate1LinearState(), input_keys=['ik_link', 'poses'], output_keys=[], visualize = _pos.visualize)
    #sm.userdata.poses = PoseArray()
    #sm.userdata.poses.header.frame_id = 'base_link'
    #sm.userdata.poses.poses = poses
    #sm.userdata.ik_link = 'r2_ee' 
    
    #with sm:
        #smach.Sequence.add('POSE_BUFFER', PoseBufferState(), transitions={'aborted':'POWER_OFF'})
        #smach.Sequence.add('GOTO', sm_plan, transitions={'aborted':'POSE_BUFFER', 'succeeded':'POSE_BUFFER'},
                           #remapping={'goal':'pose'})
        #smach.Sequence.add('POWER_OFF', SetServoPowerOffState())

    #sis = smach_ros.IntrospectionServer(name, sm, '/SM_ROOT')
    #sis.start()
    ##os.system('clear')
    #outcome = sm.execute()
    #sis.stop()
