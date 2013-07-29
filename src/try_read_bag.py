#!/usr/bin/env python
import rosbag
bag = rosbag.Bag('tricko0.bag')
for topic, msg, t in bag.read_messages(topics=['/joint_states',]):
    print '{} \n {} \n {} \n '.format(topic, msg ,t)
bag.close()
