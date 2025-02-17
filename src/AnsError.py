import pandas as pd
from src.Rango import Rango
#mport FuncionMatematica as fm

class AnsError:
    
    def calc_Xr(self,Rango: Rango):
        return ((Rango.X1 + Rango.Xu) / 2)
        

    def calc_f(self,funcion, X):
        return funcion(X)
    
    def calc_Es(self,n):
        #return (0.5e(2-n))
        return abs((0.5 * (10**(2-n))))
    
    #Ea se calcula con el valor de Xr y Xr anterior
    def calc_Ea(self, Xr, XrA):
        return abs(((Xr - XrA) * (100))/(Xr))
        

    def biseccion(self,funcion, Rango,Es,Xra,contador = 1):
        Xr = self.calc_Xr(Rango)
        mult_funciones = funcion(Rango.X1) * funcion(Xr)
        if(contador != 0):
            Ea = self.calc_Ea(Xr,Xra)
            if(Ea <= Es):
                return Xr, contador        
        if(mult_funciones) < 0:
            Rango.Xu = Xr
        elif (mult_funciones) > 0:
            Rango.X1 = Xr
       
        return self.biseccion(funcion,Rango,Es,Xr,contador + 1)


   

