import sys
sys.path.append("/home/pi/Raspi-MotoHAT-python3/Raspi-MotorHAT-python3/")
from Raspi_PWM_Servo_Driver import PWM
import time 

class Controll_Servo(object):

    ADDRESS=0x60
    FREQUENCY=60 #defult 60 Hz

    def __init__(self,**kwage):
        
        self.ADDRESS=kwage["address"]
        self.FREQUENCY=kwage["freq"]
        self.pwm=self.Setup_Servo()
        self.pwm.setPWMFreq(self.FREQUENCY)

    def Setup_Servo(self):
        return PWM(self.ADDRESS)

    def Set_PWM_ARM(self,number):
        self.pwm.setPWM(0,0,number)

    def Set_PWM_TONG(self,number):
        self.pwm.setPWM(1,0,number)
        
