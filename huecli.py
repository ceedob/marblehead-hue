#A Command Line Interface (CLI) for Philips Hue using Pyhue and Python. Totally useless but an excuse to get some experiance with Pyhue and such...
#TODO: make a directory of colours that it can understand, create a clean means of connecting the bridge

import pyhue, sys, random, time

#bridge = pyhue.Bridge('192.168.1.32', 'J4wVejuDoOvrW4TlOdGgv-2mrNVokM-0KwGtyaRm')
bridge = pyhue.Bridge('192.168.1.82', 'JaiTE2tcfSTd2l7A3FKvn1O8sskGYlbxf9fr5dRi')

def setLightHue(light, hue):
    light.on = True
    light.hue = hue

while True:
    command = raw_input("Please enter a command, type 'help' for a list of commands: ")

    if command == "off":
        for light in bridge.lights :
          light.on = False

    elif command == "on":
        for light in bridge.lights :
          light.on = True

    elif command == "party":
        bpm = int(raw_input("Enter the BPM of your party: "))
        while True:
            for light in bridge.lights :
               colour = random.randint(0, 65535)
               setLightHue(light,colour)
               print("Set "+str(colour))
               time.sleep(1/bpm)

    elif command == "exit":
        sys.exit()
