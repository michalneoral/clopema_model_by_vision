clear rosbag_wrapper;
clear ros.Bag;
clear all;
clc;
addpath(genpath('/usr/local/MATLAB/R2012b/toolbox/rosbag/'));
addpath(genpath('/home/neosh/opencv-2.4.6.1/mexopencv'));
%addpath(genpath('/home/neosh/opencv-2.4.6.1'));
path_to_bag_files = ('/media/5FB92F7D501A5B3A/Clopema/');

topics = loadTopic('topics.txt');

disp('Init startup - [ OK ]');