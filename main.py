from lib.Control import Controll_Motor
import time 


if __name__ == "__main__" :
    a=Controll_Motor(address=0x60)
    a.set_Motor2zero()
    while(True):
     a.setup_motor(1,600)
     a.forward
     time.sleep(5)
     a.backward
     time.sleep(5)
