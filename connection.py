import serial
import time

serial_path = 'COM3'
baud_rate = 115200


class Connection:
    def __init__(self):
        try:
            self.ser = serial.Serial(serial_path, baud_rate, timeout=1)
            print("Connected")
        except Exception as e:

            print(f"Error encountered during connection: {e}")
            
    def send(self, data):
        formatted = data + "\n"
        try:
            time.sleep(2)
            self.ser.write(formatted.encode())
            print(f"Sent command {data}")
            time.sleep(1)
            response = self.ser.read(64)
            print(f"Response: {response}")
            time.sleep(2)

        except Exception as e:
            print(f"Error : {e}")
            print(f"Error encountered during GCode send: {data}")


    

