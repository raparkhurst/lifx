#!/usr/bin/env python

import optparse
import sys

try:
    __import__('lifxlan')
except ImportError:
    print("Error:  Unable to import lifxlan module!")
    sys.exit(1)

from lifxlan import *



def setLightIntensity(dimPercentage):
    return 65535 * dimPercentage



if __name__=="__main__":
    parser = optparse.OptionParser()
    parser.add_option('-m',
                      help="Lifx bulb MAC address",
                      default=None,
                      dest="LightMAC")
    parser.add_option('-i',
                      help="Lifx bulb IP Address",
                      default=None,
                      dest="LightIP")
    parser.add_option('-H',
                      help="Light Hue (defaults to 0)",
                      default=0,
                      dest="LightHue")
    parser.add_option('-S',
                      help="Light Saturation (defaults to 0)",
                      default=0,
                      dest="LightSaturation")
    parser.add_option('-B',
                      help="Light Brightness, measured between 0.0 and 1.0",
                      default=1.0,
                      dest="dimPercentage")
    parser.add_option('-K',
                      help="Kelvin (2500 - 9000), defaults to 7000",
                      default=7000,
                      dest="LightKelvin")
    parser.add_option('-d',
                      help="Set to DAY mode.  Same as: -H0 -S0 -B1.0 -K7000",
                      default=False,
                      action="store_true",
                      dest="DayMode")
    parser.add_option('-e',
                      help="Set to EVENING mode.  Same as: -H0 -S0 -B0.7 -K4500",
                      default=False,
                      action="store_true",
                      dest="EveningMode")
    parser.add_option('-n',
                      help="Set to NIGHT mode.  Same as: -H0 -S0 -B0.5 -K3500",
                      default=False,
                      action="store_true",
                      dest="NightMode")
    parser.add_option('-P',
                      help="Probe Lights.  Do this if you don't know your MAC/IP address",
                      default=False,
                      action="store_true",
                      dest="ProbeLights")



    options, remainder = parser.parse_args()

    parser.parse_args()


    lan = LifxLAN()
    #LightMAC = options.LightMAC
    #LightIP = options.LightIP

    if options.ProbeLights is True:
        print("Probing lights...")
        devices = lan.get_lights()
        for d in devices:
            print(d)
        sys.exit(0)


    if options.DayMode is True:
        light = Light(options.LightMAC, options.LightIP)
        LightHue = 0
        LightSaturation = 0
        LightIntensity = setLightIntensity(1.0)
        LightKelvin = 7000

        light.set_color([LightHue,LightSaturation,LightIntensity,LightKelvin])
        sys.exit(0)


    if options.EveningMode is True:
        light = Light(options.LightMAC, options.LightIP)
        LightHue = 0
        LightSaturation = 0
        LightIntensity = setLightIntensity(0.7)
        LightKelvin = 4500

        light.set_color([LightHue,LightSaturation,LightIntensity,LightKelvin])
        sys.exit(0)

    if options.NightMode is True:
        light = Light(options.LightMAC, options.LightIP)
        LightHue = 0
        LightSaturation = 0
        LightIntensity = setLightIntensity(0.5)
        LightKelvin = 3500

        light.set_color([LightHue,LightSaturation,LightIntensity,LightKelvin])
        sys.exit(0)

    else:
        light = Light(options.LightMAC, options.LightIP)
        LightIntensity = setLightIntensity(0.5)

        LightHue = options.LightHue
        LightSaturation = options.LightSaturation
        LightKelvin = options.LightKelvin

        light.set_color([LightHue,LightSaturation,LightIntensity,LightKelvin])


    print("done")