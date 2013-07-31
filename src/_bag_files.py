#!/usr/bin/env python
"""Functions for work with bag files"""
import os, glob, time, operator
import signal
import subprocess
import string

path_to_files = '/media/5FB92F7D501A5B3A/Clopema/'

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
    name_of_file=''.join([path_to_files, name, '_', speed, '_', str(number), '_', subname])
    p = subprocess.Popen(['rosbag', 'record', '-a', '-O', name_of_file])
    return p.pid
    
def stop_bag_file(pid, time_more):
    time.sleep(time_more)
    os.kill(pid, signal.SIGINT)
