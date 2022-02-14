"""!
@file user_interface.py
This file contains the user interface which will run on the PC and send serial
input to the Nucleo and read back serial output. Plots RC circuit step response
of ADC output created from main.py.
@author Christian Clephan
@author Kyle McGrath
@date   10-Jan-2022
@copyright (c) 2022 released under CalPoly
"""


import serial
from matplotlib import pyplot

with serial.Serial ('COM4', 115200) as s_port:
    s_port.write(b'\x03')
    s_port.write(b'\x04')
    line = s_port.readline()
    time = []
    ADC_val = []
    
    #Reads through lines of main.py from Nucleo until it finds Stop
    while not b'Stop' in line:
        try:
            ADC_val.append(float(line))
        except IndexError as error:
            print(error, line)
            #print(line)
            pass
        except ValueError as error:
            print(error, line)
        finally:
            line = s_port.readline()
    for s in range(0,1000):
        time.append(s)
    pyplot.plot(time, ADC_val)
    pyplot.xlabel('Time (ms)')
    pyplot.ylabel('ADC')
    pyplot.title('RC Circuit Step Response')
    pyplot.grid(True)
    pyplot.show()