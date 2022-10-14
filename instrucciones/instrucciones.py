from abc import ABC, abstractmethod 

class instrucciones(ABC):
    def __init__(self, fila, columna):
        self.fila =fila
        self.comlumna = columna
        self.etiquetaSalida = None
        self.etiquetaContinua = None
        self.etiquetaReturn = None
        self.tempRetorno = None
        super().__init__()
    
    @abstractmethod
    def ejecutar(ambito):
        pass
    
    @abstractmethod
    def traducir(arbol,tabla):
        pass

    def eSalida(self):
        return self.etiquetaSalida

    def eSetSalida(self, s):
        self.etiquetaSalida = s

    def eSetReturn(self, s):
        self.etiquetaReturn = s

    def eContinua(self):
        return self.etiquetaContinua

    def eSetTemporal(self, s):
        self.tempRetorno = s

    def eTemporal(self):
        return self.tempRetorno

    def eReturn(self):
        return self.etiquetaReturn

    def eSetContinua(self, s):
        self.etiquetaContinua = s
