from colors import Colors
from connection import Connection
import config
import numpy as np
import sys

import time
import numpy.typing as npt


class Renderer:
    def __init__(self, arr2D: np.ndarray):
        self.arr2D: np.ndarray = arr2D
        assert len(arr2D.shape) == 2

    def render(self):
        connection = Connection()
        connection.send("M18 S60")
        # connection.send("G0 Z650") # reintroduction of rod
        # connection.send("G0 Z100")
        connection.send(f"M203 Z{config.z_speed}")
        connection.send("G28 Z")
        time.sleep(1)
        connection.send("G28 X Y") # Home all axes

        # time.sleep(2)
        # connection.send("M17") # Enable steppers
        # connection.send("M206 Z-800")
        # home offsets
        connection.send("M206 X-1")
        connection.send("M206 Y-80")
        connection.send("M206 Z-4")
        # connection.send("M503")
        # connection.send(f"M220 S{config.feedrate}")
        connection.send(f"M203 X{config.xy_speed}, Y{config.xy_speed}, Z{config.z_speed}")

        # connection.send("G0 Y2000")
        
        for y in range(config.y_points):
            for x in range(config.x_points):

                z = self.arr2D[x, y]
                # X and Y values will need to be compensated for physical dimensions by multiplying by total axis length (in mm)
                # connection.send(f"M220 S{config.feedrate}")
                connection.send(f"G0 X{x * config.x_length / config.x_points} Y{y * config.y_length / config.y_points}") # Move XY gantry
                print(f"Rendering: X{x}, Y{y}")
                print(f"At: X{x * config.x_length / config.x_points} Y{y * config.y_length / config.y_points}")
                # connection.send(f"M220 S{config.z_feedrate}")

                # SWAP THESE FOR NORMAL BEHAVIOR
                connection.send(f"G0 Z{z * config.z_height}") # Move linear actuator as Z axis
                # connection.send(f"G0 Z10")

                connection.send("G0 Z0") # Return to z = 0
                
                # print(self.arr2D[x, y])

                # try:
                #     z = self.arr2D[x, y]
                #     # X and Y values will need to be compensated for physical dimensions by multiplying by total axis length (in mm)
                #     connection.send(f"G0 X{x} Y{y}") # Move XY gantry
                #
                #     connection.send(f"G0 Z{z}") # Move linear actuator as Z axis
                #     connection.send("G0 Z0") # Return to z = 0
                #
                #     # print(self.arr2D[x, y])
                # except KeyboardInterrupt:
                #     connection.send("M18") # disable steppers on emergency exit
                #     print(Colors.RED + "Emergency Stop Triggered" + Colors.RESET + " | Steppers Disabled")
                #     sys.exit()

            print('\n')
            ready = False
            while(not ready):
                print("checking state")
                if ("busy" not in connection.get_state() and "processing" not in connection.get_state()):
                    ready = True
                    print("State ready confirmed")
                time.sleep(3)
            time.sleep(2)

        print("Render complete")
        connection.send("M18")
        print("Steppers disabled")

