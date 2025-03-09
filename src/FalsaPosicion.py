
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
        self.__limite_superior = limite_superior

    @limite_inferior.setter
    def limite_inferior(self, limite_inferior):
        self.__limite_inferior = limite_inferior


class FalsaPosicion:
    
    def calc_Es(self, n):
        return abs((0.5) * pow(10, 2 - n))
    
    def calc_Ea(self, Xr, XrA):
        return abs(((Xr - XrA) * (100))/(Xr))
    
    def calc_Xr(self, rango: Rango, funcion):
        return ((rango.limite_superior) - ((funcion(rango.limite_superior) * (rango.limite_inferior - rango.limite_superior))/((funcion(rango.limite_inferior)) - (funcion(rango.limite_superior)))))
    
    def calc_false_position(self, funcion, rango: Rango,es, Xra = 0, contador = 1):
        try:
            Xr = self.calc_Xr(rango,funcion)
            mult_funciones = funcion(rango.limite_inferior) * funcion(Xr)
            if(contador > 1):
                Ea = self.calc_Ea(Xr, Xra)
                if(Ea <= es):
                    return Xr, contador

            if mult_funciones == 0:
                return Xr, contador
            elif mult_funciones > 0:
                rango.limite_inferior = Xr
            else:
                rango.limite_superior = Xr

            return self.calc_false_position(funcion, rango, es, Xr, contador +1)
        except:
            print(f"Error Posible: PILA -- ", contador)


        