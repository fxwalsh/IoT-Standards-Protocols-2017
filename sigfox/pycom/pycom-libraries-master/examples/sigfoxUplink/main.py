from network import Sigfox
import socket
import machine
from machine import Timer

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)



led=machine.Pin("G16",machine.Pin.OUT)
button=machine.Pin("G17",machine.Pin.IN, pull=machine.Pin.PULL_UP)

def handler(button):
    machine.disable_irq()
    led.toggle()
    time.sleep(.2)
    machine.enable_irq()

irq=button.callback(machine.Pin.IRQ_FALLING, handler)


# send some bytes
s.send(bytes([0x01, 0x02, 0x03]))
