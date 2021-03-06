#!/usr/bin/env python
#
# PyUSBtmc
# display_channel.py
#
# Copyright (c) 2011 Mike Hadmack
# Copyright (c) 2010 Matt Mets
# This code is distributed under the MIT license
#
#  This script is just to test waverunner functionality as a module
#
import numpy
from matplotlib import pyplot
import sys
import os
sys.path.append(os.path.expanduser('.'))
from waverunner import Waverunner

""" Example program to plot the Y-T data from one scope channel
    derived from capture_channel_1.py but using new interface methods """
 
# Initialize our scope
scope = Waverunner("127.0.0.1")
scope.grabData()
data1 = scope.getScaledWaveform(1)
data2 = scope.getScaledWaveform(2)

# Now, generate a time axis.
time = scope.getTimeAxis() 
 
# See if we should use a different time axis
if (time[599] < 1e-3):
    time = time * 1e6
    tUnit = "uS"
elif (time[599] < 1):
    time = time * 1e3
    tUnit = "mS"
else:
    tUnit = "S"

# close interface
scope.close()
 
# Plot the data
pyplot.plot(time,data1)
pyplot.plot(time,data2)
pyplot.title("Oscilloscope Data")
pyplot.ylabel("Voltage (V)")
pyplot.xlabel("Time (" + tUnit + ")")
pyplot.xlim(time[0], time[599])
pyplot.show()


