import math
import cexprtk

class graph:
    def __init__(self,str: f):
        
        n = 5
        self.zArray = [[0]*n]*n

        st = cexprtk.Symbol_Table({'x':1.0, 'y':1.0}, add_constants=True)
        function = cexprtk.Expression(f, st)
        # establish function as an Expression that can be evaluated


