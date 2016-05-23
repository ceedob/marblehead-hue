import pyhue, random, time

def getBridge():
    b = None
    l = None
    while b == None:
        try:
            b = pyhue.Bridge('192.168.1.82', 'JaiTE2tcfSTd2l7A3FKvn1O8sskGYlbxf9fr5dRi')
            if(b is not None): l = b.lights
        except Exception as e:
            print e
    return l

def setLightHue(light, hue):
    hue %= 65535 # hue range is 0-65535
    not_set = True
    while not_set:
        try:
            light.on = True
            light.hue = hue
        except Exception as e:
            print e
        else:
            not_set = False
color = random.randint(0, 65535);
while True:
    color+=1000
    try:
        bridge = pyhue.Bridge('192.168.1.82', 'JaiTE2tcfSTd2l7A3FKvn1O8sskGYlbxf9fr5dRi')
        print color
        for light in bridge.lights :

            setLightHue(light,color+random.randint(1000, 1000) )

        time.sleep(1.5)

    except Exception as e:
        pass
