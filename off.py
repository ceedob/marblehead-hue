import pyhue

bridge = pyhue.Bridge('192.168.1.82', 'JaiTE2tcfSTd2l7A3FKvn1O8sskGYlbxf9fr5dRi')

for light in bridge.lights :
  light.on = False
