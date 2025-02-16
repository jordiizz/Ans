class FuncionMatematica:
    
    def __init__(self, funcion):
        """_summary_

        Args:
            funcion (_funcion_): _Pasamos la funcion como param, Abstraemos, encapsulamos, enfocamos OOP_
        """
        self.__funcion = funcion

    @property
    def funcion(self):
        return self.__funcion
    
    @funcion.setter
    def funcion(self, funcion):
        self.__funcion = funcion
        