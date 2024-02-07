import serial
import time

serial_path = ''
baud_rate = 0000


class Connection:
    def __init__(self):
        try:
            self.ser = serial.Serial(serial_path, baud_rate, timeout=1)
        except Exception as e:
            print(f"Error encountered during connection: {e}")
            
    def send(self, data):
        try:
            self.ser.write(data)
        except:
            print(f"Error encountered during GCode send: {data}")
    

