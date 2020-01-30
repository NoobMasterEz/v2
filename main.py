from lib.Control import Controll_Motor
from lib.Servo_Control import Controll_Servo
import cv2
import time
import tty, sys, termios
import select
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(14, GPIO.IN)    # set GPIO25 as input (button)

def setup_term(fd, when=termios.TCSAFLUSH):
    mode = termios.tcgetattr(fd)
    mode[tty.LFLAG] = mode[tty.LFLAG] & ~(termios.ECHO | termios.ICANON)
    termios.tcsetattr(fd, when, mode)

def getch(timeout=None):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        setup_term(fd)
        try:
            rw, wl, xl = select.select([fd], [], [], timeout)
        except select.error:
            return
        if rw:
            return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)



if __name__ == "__main__" :
    a=Controll_Motor(address=0x60)
    b=Controll_Servo(address=0x60,freq=60)
    a.set_Motor2zero()
    status=GPIO.input(14)
    
    while(True):
     key=getch();
     print(key,status)
     a.setup_motor(1,4,600)
     if key == "q" :
      break
     elif key == "c":
      a.stop
     elif key== "i":
      a.forward
     elif key== "k":
      a.backward
     elif key == "j":
      a.left
     elif key== "l":
      a.rigth
     elif key == "z":
      b.Set_PWM_ARM(600)
     elif key == "x":
      b.Set_PWM_ARM(150)
     elif key == "a" :
      b.Set_PWM_TONG(600)
     elif key == "s":
      b.Set_PWM_TONG(150)
     
