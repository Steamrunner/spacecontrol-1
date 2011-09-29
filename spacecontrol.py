from time import sleep
from serial import Serial

SERIAL_PORT = "/dev/tty.usbserial-A6008cOY"

class SpaceControl(object):
    TIMEOUT = 0.5

    def __init__(self, serial_port, about_rate):
        #self.serial = Serial(serial_port, about_rate)
        #self.serial.open()
        pass

    def _relay_cmd(self, id, state):
        self.serial.write("%"+str(id)+"#"+str(state))
        sleep(self.TIMEOUT)

    def button(self, id):
        self._relay_cmd(id, 0)
        self._relay_cmd(id, 1)

    def switch(self, id, powered):
        state = 0 if powered else 1
        self._relay_cmd(id, state)

    def close(self):
        #self.serial.close()
        pass

