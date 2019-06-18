#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import time

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32,queue_size=1)
rate= rospy.Rate(10)
i = 0

while not rospy.is_shutdown():
    
    pub.publish(i)
    rate.sleep()
    

    i = input('please input:')
    print('output is:',str(i))

