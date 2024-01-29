import math
import cexprtk
import matplotlib
import numpy as np


# set this value to number of discrete points in physical system
global num_points_x, num_points_y 
num_points_x: int = 10
num_points_y: int = 10
st = cexprtk.Symbol_Table({'x':1.0, 'y':1.0}, add_constants=True)

class Graph:
    def __init__(self,funct):
        self.x_step = 1
        self.y_step = 1

        
        n = 5
        # self.z_array = [[0]*num_points_x]*num_points_y
        self.array = np.zeros((num_points_x, num_points_y))


        self.parsed_function = cexprtk.Expression(funct, st)
        # establish function as an Expression that can be evaluated

    def f(self, x, y):
        st.variables['x'] = x # possible source of errors
        st.variables['y'] = y
        return self.parsed_function()

    def fill(self, x_min, x_max, y_min, y_max):
        x_step = (x_max - x_min) / num_points_x
        print(f"x step set to {x_step}")
        y_step = (y_max - y_min) / num_points_y

        for x in range(0, num_points_x, 1):
            for y in range(0, num_points_y, 1):
                self.array[x,y] = self.f(x_min + x * x_step, y_min + y * y_step)
                # print(f"Filled {x}, {y} with f of {x_min + x * x_step}, {y_min + y * y_step} = {self.f(x_min + x * x_step, y_min + y * y_step)}")
                # print(np.matrix(self.array))
        # print(np.matrix(self.array))




