# Dependencies
import math
import numpy as np

# Classes
from graph import Graph
import renderer

raw_function = input("Enter your function: f(x,y)=")


graph3D = Graph(raw_function)
graph3D.fill(0, 10, 0, 10) # x max, x min, y max, y min
print(np.matrix(graph3D.array))

#model = renderer
#renderer.__init__(model,graph3D.zArray)
#render(model)

