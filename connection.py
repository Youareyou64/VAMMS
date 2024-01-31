import serial
import time

serial_path = ''
baud_rate = 0000


class Connection:
    def __init__(self):
        self.ser = serial.Serial(serial_path, baud_rate, timeout=1)

    def send(self, data):
        self.ser.write(data)
    

