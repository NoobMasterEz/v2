import sys
sys.path.append("/home/pi/Raspi-MotorHAT-python3/Raspi-MotorHAT-python3")
from Raspi_MotorHAT import Raspi_MotorHAT , Raspi_DCMotor
import time
import atexit

class Controll_Motor(object):

    ADDRESS=0x60
    myMotor=None
    myMotor1=None

    def __init__(self,**kwage):
        """
        :address :SetDefult Address to  x60

        """
        self.ADDRESS=kwage["address"]
        self.mh=Raspi_MotorHAT(self.ADDRESS)
        self.mh1=Raspi_MotorHAT(self.ADDRESS)
        atexit.register(self.set_Motor2zero)

    
    def set_Motor2zero(self):
        for i in range(1,4):
            self.mh.getMotor(i).run(Raspi_MotorHAT.RELEASE)
    

    def setup_motor(self,number_motor,number_motor1,speed=100):
        self.myMotor=self.mh.getMotor(number_motor)
        self.myMotor1=self.mh1.getMotor(number_motor1)
        self.myMotor1.setSpeed(speed)
        self.myMotor.setSpeed(speed)

    def _decorator(foo):
        def show(self):
            foo(self)
        return show

    @property
    @_decorator 
    def forward(self):
        self.myMotor.run(Raspi_MotorHAT.FORWARD)
        self.myMotor1.run(Raspi_MotorHAT.FORWARD)
        print("[+]-Forward")

    @property
    @_decorator
    def backward(self):
        self.myMotor.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor1.run(Raspi_MotorHAT.BACKWARD)
        print("[+]-Backward") 

    @property
    @_decorator
    def left(self):
        self.myMotor.run(Raspi_MotorHAT.BACKWARD)
        self.myMotor1.run(Raspi_MotorHAT.FORWARD)
        print("[+]-Left")

    @property
    @_decorator
    def rigth(self):
        self.myMotor.run(Raspi_MotorHAT.FORWARD)
        self.myMotor1.run(Raspi_MotorHAT.BACKWARD)
        print("[+]-Rigth")

    @property
    @_decorator
    def stop(self):
        self.myMotor.run(Raspi_MotorHAT.RELEASE)
        self.myMotor1.run(Raspi_MotorHAT.RELEASE)
        print("[-]-Stop")
