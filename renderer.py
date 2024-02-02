from connection import Connection
import config
import numpy as np
import numpy.typing as npt


class Renderer:
    def __init__(self, arr2D: np.ndarray):
        self.arr2D: np.ndarray = arr2D
        assert len(arr2D.shape) == 2

    def render(self):
        connection = Connection()

        connection.send("G28") # Home all axes
        
        
        for x in range(config.x_points):
            for y in range(config.y_points):
                z = self.arr2D[x, y]
                # X and Y values will need to be compensated for physical dimensions
                connection.send(f"G0 X{x} Y{y}") # Move XY gantry
                
                connection.send(f"Z{z}") # Move linear actuator as Z axis
                
                print(self.arr2D[x, y])
            print('\n')

