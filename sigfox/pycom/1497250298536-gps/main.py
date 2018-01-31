import time


import utils
import pycom
from machine import Timer
from network import WLAN
import network



print('GPS TEST')


#activate the Terminal output of GPS sentences
#utils.GPSDEBUG=True


#activate the Thread used by GPS  'M6N' or 'G76-L'
utils.GPSstart('G76-L')


while True:
#        clear le Result Blutooth

    if utils.GPS_Is_Fixed==True :
        
            print(utils.GPSlat)
            print(utils.GPSlon)
    else:
        print ('No Sat')
        
    timer.sleep(5)
        
