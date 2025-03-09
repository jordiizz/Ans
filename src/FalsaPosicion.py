
class Rango:
    def __init__(self, limite_inferior, limite_superior):
        self.__limite_inferior = limite_inferior
        self.__limite_superior = limite_superior
    
    @property
    def limite_superior(self):
        return self.__limite_superior
    
    @property
    def limite_inferior(self):
        return self.__limite_inferior

    @limite_superior.setter
    def limite_superior(self, limite_superior):
        self.__limite_superior

    @limite_inferior.setter
    def limite_inferior(self, limite_inferior):
        self.__limite_inferior = limite_inferior


class FalsaPosicion:
    
    def calc_false_position(self, rango: Rango):
        pass

    def calc_Es(self, n):
        return abs((0.5) * pow(10, 2 - n))
    
    def calc_Ea(self, Xr, XrA):
        return abs(((Xr - XrA) * (100))/(Xr))
    
    def calc_Xr(self, rango: Rango, funcion):
        return (rango.limite_superior) - ((funcion(rango.limite_superior) * (rango.limite_inferior - rango.limite_superior))/((funcion(rango.limite_inferior)) - (funcion(rango.limite_superior))))
    

        