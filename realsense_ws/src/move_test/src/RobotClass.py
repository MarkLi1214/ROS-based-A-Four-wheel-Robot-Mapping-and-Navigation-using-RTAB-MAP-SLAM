import traitlets
import time
import math
from traitlets.config.configurable import SingletonConfigurable
from drivers import PCA9685, Motor

class Robot(SingletonConfigurable):
    
    front_left_motor = traitlets.Instance(Motor)
    front_right_motor = traitlets.Instance(Motor)
    back_left_motor = traitlets.Instance(Motor)
    back_right_motor = traitlets.Instance(Motor)

    # config
    front_left_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    front_left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    front_right_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    front_right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    back_left_motor_channel = traitlets.Integer(default_value=3).tag(config=True)
    back_left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    back_right_motor_channel = traitlets.Integer(default_value=4).tag(config=True)
    back_right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    
    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.left_motor_driver = PCA9685(0x41, debug=False)
        self.right_motor_driver = PCA9685(0x40, debug=False)
        self.front_left_motor = Motor(self.left_motor_driver, channel=self.front_left_motor_channel, alpha=self.front_left_motor_alpha)
        self.front_right_motor = Motor(self.right_motor_driver, channel=self.front_right_motor_channel, alpha=self.front_right_motor_alpha)
        self.back_left_motor = Motor(self.left_motor_driver, channel=self.back_left_motor_channel, alpha=self.back_left_motor_alpha)
        self.back_right_motor = Motor(self.right_motor_driver, channel=self.back_right_motor_channel, alpha=self.back_right_motor_alpha)
        
    def set_motors(self, front_left_speed, front_right_speed, back_left_speed, back_right_speed):
        self.front_left_motor.value = front_left_speed
        self.front_right_motor.value = front_right_speed
        self.back_left_motor.value = back_left_speed
        self.back_right_motor.value = back_right_speed
    
    def move_test(self,X,Z):
        lw=X-Z*0.115/0.12
        rw=X+Z*0.115/0.12
        #if(abs(lw)>0.5 and abs(rw)>0.5):
            #rw,lw=0.5,0.5
        #elif(abs(lw)>0.5):
            #dcddd
        if(-0.3<Z<0.3):
            print('should go stright')
            self.front_left_motor.value =X 
            self.front_right_motor.value =X
            self.back_left_motor.value = X
            self.back_right_motor.value =X
        elif(-1<Z<-0.3):# turn right
            print('should turn right')
            #if(abs(lw)<0.28 and lw<0):
                #lw=-0.28
            #elif(abs(lw)<0.28 and lw>0):
               # lw=0.28

           # if(abs(rw)<0.28 and rw<0):
               # rw=-0.28
           # elif(abs(rw)<0.28 and rw>0):
               # rw=0.28
            self.front_left_motor.value =lw
            self.front_right_motor.value =-rw
            self.back_left_motor.value =lw
            self.back_right_motor.value =-rw
        elif(0.3<Z<1): # turn left
            print('should turn left')
            #if(abs(lw)<0.28 and lw<0):
                #lw=-0.28
            #elif(abs(lw)<0.28 and lw>0):
                #lw=0.28

            #if(abs(rw)<0.28 and rw<0):
                #rw=-0.28
            #elif(abs(rw)<0.28 and rw>0):
                #rw=0.28
            self.front_left_motor.value =-lw
            self.front_right_motor.value =rw
            self.back_left_motor.value =-lw
            self.back_right_motor.value =rw
        print('Lw speed is-------------',self.front_left_motor.value)
        print('Rw speed is-------------',self.front_right_motor.value)
        print('=============================================')

        
            
    def forward(self, speed=1.0):
        if(speed>0):
            self.front_left_motor.value = speed
            self.front_right_motor.value = speed
            self.back_left_motor.value = speed
            self.back_right_motor.value = speed
            
        else:     
            self.front_left_motor.value = -speed
            self.front_right_motor.value = -speed
            self.back_left_motor.value = -speed
            self.back_right_motor.value = -speed
 
    def backward(self, speed=1.0):
        self.front_left_motor.value = -speed
        self.front_right_motor.value = -speed
        self.back_left_motor.value = -speed
        self.back_right_motor.value = -speed

    def left(self, speed=1.0):
        self.front_left_motor.value = -speed
        self.front_right_motor.value = speed
        self.back_left_motor.value = -speed
        self.back_right_motor.value = speed

    def right(self, speed=1.0):
        self.front_left_motor.value = speed
        self.front_right_motor.value = -speed
        self.back_left_motor.value = speed
        self.back_right_motor.value = -speed

    def stop(self):
        self.front_left_motor.value = 0
        self.front_right_motor.value = 0
        self.back_left_motor.value = 0
        self.back_right_motor.value = 0
    
    def forward_left(self, speed=1.0):
        self.front_left_motor.value = speed / 3
        self.front_right_motor.value = speed
        self.back_left_motor.value = speed / 3
        self.back_right_motor.value = speed
            
    def forward_right(self, speed=1.0):
        self.front_left_motor.value = speed
        self.front_right_motor.value = speed / 3
        self.back_left_motor.value = speed
        self.back_right_motor.value = speed / 3

    def backward_left(self, speed=1.0):
        self.front_left_motor.value = -speed / 3
        self.front_right_motor.value = -speed
        self.back_left_motor.value = -speed / 3
        self.back_right_motor.value = -speed
            
    def backward_right(self, speed=1.0):
        self.front_left_motor.value = -speed
        self.front_right_motor.value = -speed / 3
        self.back_left_motor.value = -speed
        self.back_right_motor.value = -speed / 3
