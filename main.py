# Dependencies
import math
import numpy as np
from connection import Connection
from graph import Graph
from renderer import Renderer


raw_function = input("Enter your function: f(x,y)=")
x_min = int(input("Minimum x value (inclusive): ")) or 0
x_max = int(input("Maximum x value (exclusive): ")) or 10
y_min = int(input("Minimum y value (inclusive): ")) or 0
y_max = int(input("Maximum y value (exclusive): ")) or 10


def generate_graph(function, x_min, x_max, y_min, y_max):
    graph = Graph(function)
    graph.fill(x_min, x_max, y_min, y_max)  # x max, x min, y max, y min
    graph.scale()

    renderer = Renderer(graph.scaled_array)
    renderer.render()
    


generate_graph(raw_function, x_min, x_max, y_min, y_max)


# graph3D = Graph(raw_function)
# graph3D.fill(0, 10, 0, 10) # x max, x min, y max, y min
# print(np.matrix(graph3D.array))

#model = renderer
#renderer.__init__(model,graph3D.zArray)
#render(model)

