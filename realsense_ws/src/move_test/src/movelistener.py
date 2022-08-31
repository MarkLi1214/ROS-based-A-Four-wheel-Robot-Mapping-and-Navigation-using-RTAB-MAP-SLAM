#!/usr/bin/env python3

import rospy
from RobotClass import Robot
import time

#initialize the Robot class
robot = Robot()
from geometry_msgs.msg import Twist

def move():
    while(True):
        #robot.move_test(0.241,0.578)    
        robot.forward(0.2)
        #time.sleep(0.1)
        robot.stop()

    
  

if __name__=="__main__":
    move()
