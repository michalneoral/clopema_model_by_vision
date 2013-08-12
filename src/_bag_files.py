#!/usr/bin/env python
"""Functions for work with bag files"""
import os, glob, time, operator
import signal
import subprocess
import string

#path_to_files = '/media/5FB92F7D501A5B3A/Clopema/'
path_to_files = '/home/neoral/'

#def last_name():
    #gt = operator.gt
    ##files = glob.glob.join([path_to_files ,'*.bag'])
    #files = glob.glob('/media/5FB92F7D501A5B3A/CLOPEMA/bagfiles/*.bag')
    #if not files:
        #return None
    #current_time = time.time()
    #last_file = files[0], current_time - os.path.getctime(files[0])
    #for f in files[1:]:
        #age = current_time - os.path.getctime(f)
        #if gt(age, last_file[1]):
            #last_file = f, age
    #print last_file[0]

#def delete_last():    
    #print 'nothing'
    
def start_bag_file_all(name,speed,number,subname):
    """function to save bag file
       save only topics in ./../matlab/topics.txt"""   
    #read a file with names of topics
    try:
        f = open("./matlab/topics.txt", "r")
        try:
            lines = f.readlines()            
        finally:
            f.close()
    except IOError:
        pass

    name_of_file=''.join([path_to_files, name, '_', speed, '_', str(number), '_', subname])
    m=range(0,len(lines)+4)
    m[0]='rosbag'
    m[1]='record'
    m[2]='-O'
    m[3]=name_of_file
    for i in range(0,len(lines)):
        s=str(lines[i]).strip()
        m[i+4]=s
    p = subprocess.Popen(m)
    return p.pid
    
def start_bag_file_topic(name,speed,number,subname):
    """function to save bag file
       save only topics in ./../matlab/topics.txt"""   
    #read a file with names of topics
    filename = "".join(['./matlab/topics',subname,'.txt'])
    try:
        f = open(filename, "r")
        try:
            lines = f.readlines()            
        finally:
            f.close()
    except IOError:
        pass

    name_of_file=''.join([path_to_files, name, '_', speed, '_', str(number), '_', subname])
    m=range(0,len(lines)+4)
    m[0]='rosbag'
    m[1]='record'
    m[2]='-O'
    m[3]=name_of_file
    for i in range(0,len(lines)):
        s=str(lines[i]).strip()
        m[i+4]=s
    p = subprocess.Popen(m)
    return p.pid    

def start_bag_file_camera_def(number_of_position):
    """function to save bag file
       save only topics in ./../matlab/topics.txt"""   
    try:
        f = open("./matlab/topics.txt", "r")
        try:
            lines = f.readlines()            
        finally:
            f.close()
    except IOError:
        pass

    name_of_file=''.join([path_to_files, 'camera_default', '_',number_of_position])
    m=range(0,len(lines)+4)
    m[0]='rosbag'
    m[1]='record'
    m[2]='-O'
    m[3]=name_of_file
    for i in range(0,len(lines)):
        s=str(lines[i]).strip()
        m[i+4]=s
    p = subprocess.Popen(m)
    return p.pid    
    
def stop_bag_file(pid, time_more):
    time.sleep(time_more)
    os.kill(pid, signal.SIGINT)
    
