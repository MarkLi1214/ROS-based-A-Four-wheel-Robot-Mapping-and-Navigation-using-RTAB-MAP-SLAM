#!/usr/bin/env python3

import rospy
#import tf.transformations
from geometry_msgs.msg import Twist

import time
from RobotClass import Robot

robot = Robot()

def callback(msg):
    r=rospy.Rate(30)
    #rospy.loginfo("Received a /cmd_vel message!")
    #rospy.loginfo("Linear Components: [%f, %f, %f]"%(msg.linear.x, msg.linear.y, msg.linear.z))
    #rospy.loginfo("Angular Components: [%f, %f, %f]"%(msg.angular.x, msg.angular.y, msg.angular.z))

    # Do velocity processing here:
    # Use the kinematics of your robot to map linear and angular velocities into motor commands

    #vehicle_measurements = (msg.angular.z * 0.20 )/ 2
    #robot_right = (msg.linear.x - vehicle_measurements )/ 0.6
    #robot_left =  (msg.linear.x - vehicle_measurements ) / 0.6
    
    # Then set your wheel speeds (using wheel_left and wheel_right as examples)
    #print("right wheel : " , msg.linear.x)
    print('X is--------------------:', msg.linear.x)
    print('Z is--------------------:', msg.angular.z)
    X=msg.linear.x
    Z=msg.angular.z
    lw=X-Z*0.115
    rw=X+Z*0.115
    print('Original: lw rw  is--------------------:[', lw,rw,']')
    #if(0<lw<0.2):
        #lw=0.2
    #elif(-0.2<lw<0):
        #lw=-0.2  
    if(X==0 and abs(Z)<0.3):
        rw=0
        lw=0
        robot.set_motors(lw,rw,lw,rw)
    elif(-0.15<=msg.linear.x<=0.15 and Z!=0):    # turn 
        while(abs(lw-rw)<0.1):#increase different speed of wheels
            lw=2*lw
            rw=2*rw
        while(abs(lw)<0.3 and abs(rw)<0.3):#increase speed
            print('increasing--------------')
            lw=1.5*lw
            rw=1.5*rw
        if(lw>0.45): #maximum speed
            lw-=0.15
        elif(lw<-0.45):
            lw+=0.15
        
        if(rw>0.45):
            rw-=0.15
        elif(rw<-0.45):
            rw+=0.15
            
        robot.set_motors(lw,rw,lw,rw)
        r.sleep()
        print('Rotating: lw rw  is--------------------:[', lw,rw,']')
    else:
        if(lw>0.45): #maximum speed
            lw-=0.15
        elif(lw<-0.45):
            lw+=0.15
        if(rw>0.45):
            rw-=0.15
        elif(rw<-0.45):
            rw+=0.15
        robot.set_motors(lw,rw,lw,rw)#go stright
        r.sleep()
        print('Normal--: lw rw  is--------------------:[', lw,rw,']')
    


def listener():
    rospy.init_node('cmd_vel_listener')
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()
    #r=rospy.Rate(1)
if __name__ == '__main__':
    listener()
