from connection import Connection
import config
import numpy as np
import numpy.typing as npt


class Renderer:
    def __init__(self, arr2D: np.ndarray):
        self.arr2D: np.ndarray = arr2D
        assert len(arr2D.shape) == 2

    def render(self):
        # connection = Connection()
        for x in range(config.x_points):
            for y in range(config.y_points):
                z = self.arr2D[x, y]
                print(self.arr2D[x, y])
            print('\n')
