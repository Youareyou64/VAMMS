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
        # connection.send("G0 Z100")

        connection.send("G28 X Y") # Home all axes

        # time.sleep(2)
        # connection.send("M17") # Enable steppers
        connection.send("M206 X-4")
        connection.send("M206 Y-4")
        # connection.send("M503")
        # connection.send(f"M220 S{config.feedrate}")
        connection.send(f"M203 X{config.xy_speed}, Y{config.xy_speed}, Z{config.z_speed}")

        # connection.send("G0 Y2000")
        
        for x in range(config.x_points):
            for y in range(config.y_points):

                z = self.arr2D[x, y]
                # X and Y values will need to be compensated for physical dimensions by multiplying by total axis length (in mm)
                # connection.send(f"M220 S{config.feedrate}")
                connection.send(f"G0 X{x * config.x_length / config.x_points} Y{y * config.y_length / config.y_points} F1500") # Move XY gantry

                # connection.send(f"M220 S{config.z_feedrate}")
                connection.send(f"G0 Z{-1 * z * config.z_height}") # Move linear actuator as Z axis
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

        print("Render complete")
        connection.send("M18")
        print("Steppers disabled")

