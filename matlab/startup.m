clear rosbag_wrapper;
clear ros.Bag;
clear all;
clc;
addpath(genpath('/usr/local/MATLAB/R2012b/toolbox/rosbag/'));
path_to_bag_files = ('/media/5FB92F7D501A5B3A/Clopema/');

topics = loadTopic('topics.txt');

disp('Init startup - [ OK ]');