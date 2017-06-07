#File: DLight_Sensor.py
#Course: EECS 113 Processor HW/SW Interface, Spring 2017
#Team: TrashBot
#Members:
#     Linda Vang
#     Claudia Gorgonio
#     Jun Li
#     Sandra Fong
#Description:
#     Class for Grove Digital Light Sensor

from pynq import Overlay
Overlay("base.bit").download()
from pynq.iop import grove_dlight
#REMEMBER: put grove_dlight.py and arduino_grove_dlight.bin in pynq
#from grove_dlight import Grove_DLight
#REMEMBER: put grove_dlight.py and arduino_grove_dlight.bin in juypter nootbook
from pynq.iop import PMODA
from pynq.iop import PMODB
from pynq.iop import PMOD_GROVE_G3
from pynq.iop import PMOD_GROVE_G4
import time

class DLight_Sensor(object):

    def get(self, if_id, gr_pin):
        if if_id in [PMODA, PMODB]:
            print("if_id is: ", if_id)
            if not gr_pin in [PMOD_GROVE_G3, PMOD_GROVE_G4]:
                raise ValueError("DLight group number can only be G3 - G4.")
        else:
            raise ValueError("No such IOP for grove device.")
        #lgt = grove_dlight.Grove_DLight(if_id, gr_pin)

        #read_raw_light returns 2 integer values ch0 (visible) and ch1 (IR)
        #sensor_val = lgt.read_raw_light()
        #print(sensor_val)
        #read_lux returns lux value from sensor, luminous flux per unit area
        #test_val = lgt.read_lux()
        test_val = 0
        print(test_val)
        if(test_val < 260):
            #close lid
            print("Sensor is covered")
            return 1
        else:
            #open lid
            print("Sensor is not covered")
            return 0
        print("")
        time.sleep(1)