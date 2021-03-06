from pynq import Overlay
Overlay("base.bit").download()

from pynq.iop import Pmod_PWM
from pynq.iop import PMODA
from pynq.iop import PMODB

import time

#Class for the Motor functions
#Waring for Future References: All Motors are Plastic Gear Analog Servo LS-3006

class MFunction:
    
    def __init__(self, id, period, duty):
        #ID: PMODA = 1, 2 and PMODB = 3, 4
        #pin = The pin corresponding to the PMOD
        if(id == 1):
            self.signal = Pmod_PWM(PMODA, 0)
        elif(id == 2):
            self.signal = Pmod_PWM(PMODA, 1)
        elif(id == 3):
            self.signal = Pmod_PWM(PMODB, 0)
        elif(id == 4):
            self.signal = Pmod_PWM(PMODB, 1)
        
        self.period = period
        self.duty = duty
        
        self.signal.generate(self.period, self.duty)
    
    #Functions for Steering
    def goLeft(self):
        for i in range(0, 1):
            self.signal.generate(2650, 50)
            time.sleep(.01)
    
    def goRight(self):
        for i in range(0, 1):
            self.signal.generate(4550, 98)
            time.sleep(.01)
    
    #Function for back wheel
    def goForward(self):
        for i in range(0, 1):
            self.signal.generate(2000, 50)
            time.sleep(1)
    
    def goBackward(self):
        for i in range(0, 1):
            self.signal.generate(4550, 98)
            time.sleep(1)
        
    #Function for Operating the Lid
    def openingLid(self):
        for i in range(0, 2):
            self.signal.generate(4550, 98)
            time.sleep(.1)
    
    def closingLid(self):
        for i in range(0, 2):
            self.signal.generate(2000, 50)
            time.sleep(.01)
        
    def stop(self):
        self.signal.generate(1, 1)
        self.signal.stop()

