import serial
import time

serial_path = 'COM3'
baud_rate = 9600


class Connection:
    def __init__(self):
        try:
            self.ser = serial.Serial(serial_path, baud_rate, timeout=1)
            print("Connected")
        except Exception as e:

            print(f"Error encountered during connection: {e}")
            
    def send(self, data):
        try:
            self.ser.write(data.encode())
            print(f"Sent command {data}")
        except Exception as e:
            print(f"Error: {e}")
            # print(f"Error encountered during GCode send: {data}")


    

