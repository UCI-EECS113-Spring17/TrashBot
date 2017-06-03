#File: grove_dlight_test1.py
#Course: EECS 113 Processor HW/SW Interface, Spring 2017
#Team: TrashBot
#Members:
#     Linda Vang
#     Claudia Gorgonio
#     Jun Li
#     Sandra Fong
#Description:
#     Test file for Grove Digital Light Sensor
#     Without PYNQ Grove Adapter:
#         Pins should be connected to PMODA
#         SDA Pin should be connected to pin 2
#         SCL Pin should be connected to pin 6

from pynq import Overlay
Overlay("base.bit").download()
from pynq.iop import grove_dlight
from pynq.iop import PMODA
from pynq.iop import PMOD_GROVE_G4
import time

lgt = grove_dlight.Grove_DLight(PMODA, PMOD_GROVE_G4)

for i in range(0, 50):
    print("loop: ", i)

    #read_raw_light returns 2 integer values ch0 (visible) and ch1 (IR)
    sensor_val = lgt.read_raw_light()
    print(sensor_val)
    
    #read_lux returns lux value from sensor, luminous flux per unit area
    test_val = lgt.read_lux()
    print(test_val)
    if(test_val < 260):
        print("Sensor is covered")
    else:
        print("Sensor is not covered")

    print("")
    time.sleep(1)