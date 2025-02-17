import pandas as pd
from src.Rango import Rango
#mport FuncionMatematica as fm

class AnsError:
    
    def calc_Xr(self,Range: Rango):
        return ((Range.X1 + Range.Xu) // 2)
        

    def calc_f(self,funcion, X):
        return funcion(X)

    def biseccion(self,funcion, Range: Rango,memo = {}):
        while():
            pass
        

    def valor_cercano():
        pass

