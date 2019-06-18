#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
def cb(message):
    
    flag = message.data
    if flag == 1:
        GPIO.output(2,True)
        time.sleep(3)
        GPIO.output(2,False)
    if flag == 2:
        GPIO.output(24,True)
        time.sleep(3)
        GPIO.output(24,False)
    if flag == 3:
        for i in xrange(5):
            GPIO.output(24,True)
            time.sleep(1)
            GPIO.output(24,False)
            GPIO.output(2,True)
            time.sleep(1)
            GPIO.output(2,False)
    else:
        GPIO.output(2,False)

def cb1(message):
    rospy.loginfo(message.data*2)        
        

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    rospy.spin()
    GPIO.cleanup()
