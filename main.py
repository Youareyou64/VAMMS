# VAMMS - A Project Lead The Way project
# Jack Sloan, Shawn Johnson, and Matthew Wincek
# 2023-2024

# Dependencies

import math
import numpy as np
from connection import Connection
from graph import Graph
from renderer import Renderer
import dance
from colors import Colors


raw_function = input("Enter your function: f(x,y)=")
if(raw_function) == "SJM":
    dance.dance()
    raw_function = input("Enter your function: f(x,y)=")
    
try:
    x_min = int(input("Minimum x value (inclusive): "))
except ValueError:
    x_min = 0

try:
    x_max = int(input("Maximum x value (exclusive): "))
except ValueError:
    x_max = 10

try:
    y_min = int(input("Minimum y value (inclusive): "))
except ValueError:
    y_min = 0
    
try:
    y_max = int(input("Maximum y value (exclusive): "))
except ValueError:
    y_max = 10


def clean_function(function):
    function = function.replace(" ", "")
    function = function.replace("xy", "x * y")
    function = function.replace("yx", "x * y")
    print(Colors.CYAN + f"Graphing: {function}" + Colors.RESET)

    return function


def generate_graph(function, x_min, x_max, y_min, y_max):
    graph = Graph(function)
    graph.fill(x_min, x_max, y_min, y_max)  # x max, x min, y max, y min
    graph.scale()

    renderer = Renderer(graph.scaled_array)
    renderer.render()
    

cleaned_function = clean_function(raw_function)

generate_graph(cleaned_function, x_min, x_max, y_min, y_max)



