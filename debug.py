import pyhue

bridge = pyhue.Bridge('192.168.1.82', 'JaiTE2tcfSTd2l7A3FKvn1O8sskGYlbxf9fr5dRi')

for light in bridge.lights :
  print "=== Light #"+light.id, "==="
  print "id:", light.id
  print "manufacturername:", light.manufacturername
  print "modelid:", light.modelid
  print "name:", light.name
  print "state:"
  for i in light.state:
      print "  %s:" % i, light.state[i]
  print "swversion:", light.swversion
  print "type:", light.type
  print "uniqueid:", light.uniqueid

  print
