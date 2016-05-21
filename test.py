import pyhue

bridge = pyhue.Bridge('192.168.1.82', 'chris@penguinleaf.com')

for light in bridge.lights:
    print(light)
    light.on = True
    light.hue = 0
