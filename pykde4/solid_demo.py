#!/usr/bin/env python

# [SNIPPET_NAME: Solid Demo]
# [SNIPPET_CATEGORIES: PyKDE4]
# [SNIPPET_DESCRIPTION: Demos some of the features of Solid]
# [SNIPPET_AUTHOR: Simon Edwards <simon@simonzone.com>]
# [SNIPPET_LICENSE: GPL3]
# [SNIPPET_DOCS: http://api.kde.org/pykde-4.3-api/solid/index.html]

###########################################################################
# solid_demo.py - Demonstrates use of Solid.
#
###########################################################################
# Copyright (C) 2007 Simon Edwards <simon@simonzone.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License or (at
# your option) version 3 or, at the discretion of KDE e.V. (which shall
# act as a proxy as in section 14 of the GPLv3), any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from PyKDE4.kdecore import *
from PyKDE4.solid import *

def main():
    componentData = KComponentData("solid_demo")

    print("All devices found by Solid")
    print("--------------------------")
    for device in Solid.Device.allDevices():
        print(device.udi())
    print("")
    
    print("All audio devices found by Solid")
    print("--------------------------------")
    for device in Solid.Device.listFromType(Solid.DeviceInterface.AudioInterface, ""):
        print(device.udi())
    print("")

    print("Processor found by Solid")
    print("------------------------")
    
    # Get a Processor
    device_list = Solid.Device.listFromType(Solid.DeviceInterface.Processor, "")

    # take the first processor
    device = device_list[0]
    if device.isDeviceInterface(Solid.DeviceInterface.Processor):
        print("We've got a processor! %i to be exact..." % len(device_list))
    else:
        print("Device is not a processor.")

    processor = device.asDeviceInterface(Solid.DeviceInterface.Processor)
    print("This processors maximum speed is: " + str(processor.maxSpeed()))

    extensions = processor.instructionSets()
    print("Intel MMX supported: " + ("yes" if extensions & Solid.Processor.IntelMmx else "no"))
    print("Intel SSE supported: " + ("yes" if extensions & Solid.Processor.IntelSse else "no"))
    print("Intel SSE2 supported: " + ("yes" if extensions & Solid.Processor.IntelSse2 else "no"))
    print("Intel SSE3 supported: " + ("yes" if extensions & Solid.Processor.IntelSse3 else "no"))
    print("Intel SSE4 supported: " + ("yes" if extensions & Solid.Processor.IntelSse4 else "no"))
    print("AMD 3DNOW supported: " + ("yes" if extensions & Solid.Processor.Amd3DNow else "no"))
    print("PPC AltiVec supported: " + ("yes" if extensions & Solid.Processor.AltiVec else "no"))
    print("")
    
    print("Checking network status")
    print("-----------------------")
    
    if Solid.Networking.status() == Solid.Networking.Connected:
        print("Networking is enabled.  Feel free to go online!")
    else:
        print("Network not available.")
    print("")
    
    # get a Network Device
    netlist = Solid.Device.listFromType(Solid.DeviceInterface.NetworkInterface, "")
    
    # check to see if no network devices were found
    if len(netlist)==0:
        print("No network devices found!")
    else:
        print("Found %s network device(s)" % len(netlist))
        for device in netlist:
            netdev = device.asDeviceInterface(Solid.DeviceInterface.NetworkInterface)
            
            # keep the program from crashing in the event that there's a bug in solid
            if netdev is None:
                print("Device could not be converted.  There is a bug.")
            else:
                print("The iface of %s is %s" % (str(device.udi()),str(netdev.ifaceName())))
    
main()
