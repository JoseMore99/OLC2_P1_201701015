from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito

class MatchCoin(instrucciones):
    
    def __init__(self, fila, columna,listaval,contenido):
        self.fila =fila
        self.comlumna = columna
        self.listaval = listaval
        self.contenido = contenido
        
    
    def ejecutar(self,ambito:ambito):
        aux = self.contenido.ejecutar(ambito)
        if aux is not None:
            return aux
