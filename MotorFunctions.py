from pynq import Overlay
Overlay("base.bit").download()

from pynq.iop import Pmod_PWM
from pynq.iop import PMODA
from pynq.iop import PMODB

import time

#Attempting to create a Class for the Motor functions
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
        self.signal.generate(20000, 15)
    
    def goRight(self):
        self.signal.generate(20000, 15)
    
    #Function for back wheel
    def goForward(self):
        self.signal.generate(20000, 15)
        
    #Function for Operating the Lid
    def openingLid(self):
        self.signal.generate(1, 1)
    
    def closingLid(self):
        self.signal.generate(1, 1)
        
    def stop(self):
        self.signal.generate(1, 1)
        self.signal.stop()
