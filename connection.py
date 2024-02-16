import serial
import time
from colors import Colors

serial_path = 'COM3'
baud_rate = 115200


class Connection:
    def __init__(self):
        try:
            self.ser = serial.Serial(serial_path, baud_rate, timeout=1)
            print("Connected")
        except Exception as e:

            print(Colors.RED + f"Error encountered during connection: {e}" + Colors.RESET)
            
    def send(self, data):
        formatted = data + "\n"
        success = False
        while(not success):
            try:
                time.sleep(2)
                self.ser.write(formatted.encode())
                print(Colors.GREEN + f"Sent command {data}" + Colors.RESET)
                time.sleep(1)
                response = str(self.ser.read(64))
                print(f"Response: {response}")
                if 'busy' in response or 'processing' in response:
                    success = False
                elif 'ok' in response:
                    success = True
                else:
                    print(Colors.MAGENTA + f"Unexpected GCODE Response encountered ^" + Colors.RESET)
                time.sleep(2)
    
            except Exception as e:
                print(f"Error : {e}")
                print(Colors.RED + f"Error encountered during GCode send: {data}" + Colors.RESET)
                time.sleep(5)


    

