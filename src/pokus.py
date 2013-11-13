#!/usr/bin/env python
"""Functions for work with bag files"""
import os, glob, time, operator
import signal
import subprocess
import string

path_to_files = '/media/neosh/5FB92F7D501A5B3A/Clopema/Pokusy/'
#path_to_files = '/home/neoral/'
path_to_topic = '/../matlab/topics.txt'

def start_bag_file_camera_def(number_of_position):
    """function to save bag file
       save only topics in ./../matlab/topics.txt"""   
    try:
        print "open"
        f = open(path_to_topic, "r")
        try:
            lines = f.readlines()            
        finally:
            f.close()
    except IOError:
        print lines
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
    #pro = subprocess.Popen(m, stdout=subprocess.PIPE, 
    #                   shell=True, preexec_fn=os.setsid) 
    print p.pid
    
    #print pro.pid
    return p.pid    
    
def stop_bag_file(pid, time_more):
    time.sleep(time_more)
    #os.killpg(pid, signal.SIGTERM)
    #os.kill(pid, signal.SIGINT)
    #os.kill(pid, signal.SIGTERM)

    
def main():
        pid=start_bag_file_camera_def(str(5))
        stop_bag_file(pid,2)    

if __name__ == '__main__':
    main()
