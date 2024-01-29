# Dependencies
import math

# Classes
import graph
import renderer

raw_function = input("Enter your function: f(x,y)=")


graph3D = graph
graph.__init__(graph3D, raw_function)

model = renderer
renderer.__init__(model,graph3D.zArray)
render(model)

