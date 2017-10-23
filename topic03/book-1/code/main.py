from pysense import Pysense

from LIS2HH12 import LIS2HH12

from SI7006A20 import SI7006A20

from LTR329ALS01 import LTR329ALS01

from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

import time
from network import Sigfox
import socket

py = Pysense()

mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals

si = SI7006A20(py)

lt = LTR329ALS01(py)

li = LIS2HH12(py)

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

while True:
    temperature = int(round(si.temperature()*100))
    light = lt.light()[0]
    print(str(temperature) + ":"+str(light))
    messageBytes=bytes((temperature & 0xff, ((temperature >> 8) & 0xff),light & 0xff, ((light >> 8) & 0xff)))
    s.send(messageBytes)
    time.sleep(15)
