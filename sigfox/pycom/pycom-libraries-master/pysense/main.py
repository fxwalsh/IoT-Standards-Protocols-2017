# See https://docs.pycom.io for more information regarding library specifics

from pysense import Pysense
from LIS2HH12 import LIS2HH12
from time import sleep

li = LIS2HH12(py)

while True:
    print(li.acceleration())
    print(li.roll())
    print(li.pitch())
    sleep(1)
