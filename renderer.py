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
        # connection.send("G0 Z650") # semi auto reintroduction of rod process
        # connection.send("G0 Z100")
        connection.send(f"M203 Z{config.z_speed}")
        connection.send("G28 Z")
        time.sleep(1)
        connection.send("G28 X Y") # Home all axes

        connection.send("M120") # enable endstops

        # time.sleep(2)
        # connection.send("M17") # Enable steppers
        # connection.send("M206 Z-800")
        # home offsets
        connection.send("M206 X-1")
        connection.send("M206 Y-70")
        connection.send("M206 Z-4")
        # connection.send("M503")
        # connection.send(f"M220 S{config.feedrate}")
        connection.send(f"M203 X{config.xy_speed}, Y{config.xy_speed}, Z{config.z_speed}")

        # connection.send("G0 Y2000")
        
        for y in range(0, config.y_points-1):
            for x in range(0, config.x_points):

                z = self.arr2D[x, y]

                # connection.send(f"M220 S{config.feedrate}")
                connection.send(f"G0 X{x * config.x_length / config.x_points} Y{y * config.y_length / config.y_points}") # Move XY gantry
                print(f"Rendering: X{x}, Y{y}")
                print(f"At: X{x * config.x_length / config.x_points} Y{y * config.y_length / config.y_points}")
                # connection.send(f"M220 S{config.z_feedrate}")

                # SWAP THESE FOR NORMAL BEHAVIOR
                connection.send(f"G0 Z{z * config.z_height}") # Move linear actuator as Z axis
                # connection.send(f"G0 Z10")

                connection.send("G0 Z0") # Return to z = 0
                


            print('\n')
            ready = False


            # REMOVE BELOW IF M118 DOES NOT WORK AS EXPECTED
            time.sleep(2)
            connection.send("M400") # Finish all buffered moves
            connection.send("M118 Row Complete") # Echo message for next row detection

            while(not ready):
                print(Colors.MAGENTA + "Awaiting cue to move to next row" + Colors.RESET)
                time.sleep(1)
                if (connection.is_ready_for_row()):
                    ready = True
                    print(Colors.CYAN + "Row completed, moving on" + Colors.RESET)
                else:
                    print("Row not yet complete, waiting (renderer.py line 81)")


        print("Render complete")
        connection.send("M18")
        print("Steppers disabled")

