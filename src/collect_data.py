#!/usr/bin/env python
"""program for collecting data, only menu"""
import roslib; roslib.load_manifest('clopema_smach')
import rospy, smach, smach_ros, math, copy, tf, PyKDL, os, shutil, numpy, time, subprocess
from _bag_files import start_bag_file_all, stop_bag_file
from actions import GoHome, GoToAction, ActionMove, OpenGrip, CloseGrip

time_to_close = 3
time_to_measure = 3
robot_speed = '0.1'

class bag_file_record:
    def __init__(self):
        self.subname_of_file = ''
        self.number_of_file = ''
        self.time_more = 3.0 

    def zeros(self):
        _h_num=int(self.number_of_file)
        count=0
        while _h_num >= 10:
           	_h_num = _h_num/10
           	count+=1
        s = str(int(self.number_of_file))
        for i in range(3-count):
            s=''.join(['0',s])
        self.number_of_file=s       

    def increase_number(self):
        num=int(self.number_of_file)
        num+=1
        self.number_of_file=str(num)
        self.zeros()
    
    def rename_bag(self):
        self.subname_of_file = str(raw_input('\nPut a name of file:\n'))
        while self.subname_of_file == '':
            self.subname_of_file = str(raw_input('\nPut a name of file:\n'))
        self.number_of_file = str(raw_input('\nPut a number of file:\n'))
        while self.number_of_file == '':
            self.number_of_file = str(raw_input('\nPut a number of file:\n'))
        self.zeros()

    def get_next_name(self):
        if self.subname_of_file == '' or self.number_of_file == '':
	        self.rename_bag()
        next_name='.'.join([self.subname_of_file, self.number_of_file, 'bag'])
        return next_name	

def action_record_submenu(f):
    pid=start_bag_file_all(f.subname_of_file,f.number_of_file)
    ActionMove()
    stop_bag_file(pid,f.time_more)
    f.increase_number()
    OpenGrip()

def action_record(f):
    i=raw_input("\n\n PRESS ENTER to close grip in %d seconds(...n...for exit)\n\n" % time_to_close)
    if i != 'n' and i != 'N':
        time.sleep(time_to_close)
        CloseGrip()
        i=raw_input("\n\n PRESS ENTER to action in %d seconds(...n...for open grip and exit)\n\n" % time_to_measure)
        if i != 'n' and i != 'N':
			
            time.sleep(time_to_measure)
            action_record_submenu(f)
        else:
		    OpenGrip()
		    
def _record_change_menu(i,f):
    #may do no.3 - change time
    if i=='1' or i=='rename':
        f.rename_bag()
    elif i=='2' or i=='delete':
        print 'delete_last()'
    elif i=='menu':        
        print ""
    elif i=='stop':
        exit()
    else:
	    print "Doesn't work"

def _record_change(f):
    i = raw_input ("\n...1....CHANGE NAME (rename)\n...2....DELETE LAST ONE AND CONTINUE (delete)\n..menu..EXIT from recording\n\n..stop..EXIT program\n\n")
    _record_change_menu(i,f)

def _record_menu(i,f):
    if i=='Y' or i=='y':
        action_record(f)
    else:
        _record_change(f) 
    
def _record(f):    
    i=''
    while i != 'n' and i != 'N':        
        i = raw_input ("\nFor edit [n]\nWant you record %s file? [Y/n]\n" % f.get_next_name())
        _record_menu(i,f)

def _menu(i,f):
    if i=='1' or i=='home':
        GoHome()
    elif i=='2' or i=='mpos':
        GoToAction()
    elif i=='3' or i=='action':
        _record(f)
    elif i=='stop':
        exit()
    else:
	    print "Doesn't work"

def start_program(f):
    i=''
    while i != 'stop':
        i = raw_input ("\n...1....Move to the HOME position (home)\n...2....Move to READY TO MEASURE position (mpos)\n...3....Move and record (action)\n..stop..EXIT\n\n")
        _menu(i,f)

def main():
    rospy.init_node('collect_data')
    p=subprocess.Popen(['rosservice', 'call', '/set_robot_speed', robot_speed])
    f=bag_file_record()
    print f.time_more
    start_program(f)    

if __name__ == '__main__':
    main()
