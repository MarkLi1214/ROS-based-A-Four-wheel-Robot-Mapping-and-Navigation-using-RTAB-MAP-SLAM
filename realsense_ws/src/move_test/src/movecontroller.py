#!/usr/bin/env python3



from RobotClass import Robot
import time



robot = Robot()

import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch



def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
            robot.forward(0.3)
            time.sleep(0.2)
        elif k=='\x1b[B':
            robot.backward(0.3)
            time.sleep(0.2)
        elif k=='\x1b[C':
            robot.forward_right(0.3)
            time.sleep(0.2)
        elif k=='\x1b[D':
            robot.forward_left(0.3)    
            time.sleep(0.2)
        else:
                robot.stop()



def main():
        while(1):
            get()

if __name__=='__main__':
        main()
