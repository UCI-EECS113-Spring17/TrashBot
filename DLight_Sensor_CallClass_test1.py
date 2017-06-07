#File: DLight_Sensor_test1.py
#Course: EECS 113 Processor HW/SW Interface, Spring 2017
#Team: TrashBot
#Members:
#     Linda Vang
#     Claudia Gorgonio
#     Jun Li
#     Sandra Fong
#Description:
#     Test file for Grove Digital Light Sensor Class
#     Without PYNQ Grove Adapter:
#         Pins should be connected to PMODA
#         SDA Pin should be connected to pin 2
#         SCL Pin should be connected to pin 6

from pynq import Overlay
Overlay("base.bit").download()
from DLight_Sensor import DLight_Sensor
from pynq.iop import PMODA
from pynq.iop import PMOD_GROVE_G4


test = DLight_Sensor()
test_num = test.get(PMODA, PMOD_GROVE_G4)

print(test_num)