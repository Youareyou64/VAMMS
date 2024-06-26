# series of test XY gantry moves

from connection import Connection
import config
import numpy as np
import numpy.typing as npt

def dance():
    connection = Connection()

    # connection.send("G0 X0 Y0")
    connection.send("M18 S10")
    connection.send(f"G0 X{config.x_length}")
    connection.send(f"G0 Y{config.y_length}")
    connection.send(f"G0 X0")
    connection.send(f"G0 Y0")

    connection.send(f"G0 X{config.x_length/2}")
    connection.send(f"G2 I0 J{config.y_length/2}")
    connection.send("M18")
