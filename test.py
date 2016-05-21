import pyhue, random, time

bridge = pyhue.Bridge('192.168.1.82', 'JaiTE2tcfSTd2l7A3FKvn1O8sskGYlbxf9fr5dRi')

while True:
    try:
        for light in bridge.lights:
            i = random.randint(0, 65535)
            print(i)
            light.on = True
            light.hue = i
    except Exception as e:
        print e
        time.sleep(1)
    else:
        time.sleep(0.01)
