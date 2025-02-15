class Range:
    def __init__(self,X1,Xu):
        self.__X1 = X1
        self.__Xu = Xu
    
    @property
    def X1(self):
        return self.__X1
    
    @X1.setter
    def X1(self, X1):
        self.__X1 = X1

    @property
    def Xu(self):
        return self.__Xu
    
    @Xu.setter
    def Xu(self,Xu):
        self.__Xu = Xu