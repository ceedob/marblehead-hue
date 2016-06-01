#A Command Line Interface (CLI) for Philips Hue using Pyhue and Python.
import pyhue, sys

bridge = pyhue.Bridge('192.168.1.32', 'J4wVejuDoOvrW4TlOdGgv-2mrNVokM-0KwGtyaRm')

while True:
    command = raw_input("Please enter a command, type 'help' for a list of commands: ")
    if command == "off":
        for light in bridge.lights :
          light.on = False
    elif command == "on":
        for light in bridge.lights :
          light.on = True
    elif command == "exit":
        sys.exit()
