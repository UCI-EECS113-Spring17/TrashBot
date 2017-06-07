#File: DLight_Sensor
#Course: EECS 113 Processor HW/SW Interface, Spring 2017
#Team: TrashBot
#Members:
#     Linda Vang
#     Claudia Gorgonio
#     Jun Li
#     Sandra Fong
#Description:
#     Final Class for Grove Digital Light Sensor
#To call in main file:
#	  object_variable = DLight_Sensor()
#     light_value = object_variable.get(PMODA, PMOD_GROVE_G4)

from pynq import Overlay
Overlay("base.bit").download()
from pynq.iop import grove_dlight
#REMEMBER: put grove_dlight.py and arduino_grove_dlight.bin in pynq
from pynq.iop import PMODA
from pynq.iop import PMODB
from pynq.iop import PMOD_GROVE_G3
from pynq.iop import PMOD_GROVE_G4
import time

class DLight_Sensor(object):

    def get(self, if_id, gr_pin):
        if if_id in [PMODA, PMODB]:
            if not gr_pin in [PMOD_GROVE_G3, PMOD_GROVE_G4]:
                raise ValueError("DLight group number can only be G3 - G4.")
        else:
            raise ValueError("No such IOP for grove device.")
        lgt = grove_dlight.Grove_DLight(if_id, gr_pin)

        #read_lux returns lux value from sensor, luminous flux per unit area
        sensor_val = lgt.read_lux()
        #this value -220- is dependent on the normal lighting of the room
        if(sensor_val < 220):
            #close lid - sensor is covered
            return 1
        else:
            #open lid - sensor is not covered
            return 0