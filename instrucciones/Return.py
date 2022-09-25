from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol

class Return(instrucciones):
    
    def __init__(self, fila, columna,valor=None):
        self.fila =fila
        self.columna = columna
        self.valor = valor
        
    
    def ejecutar(self,ambito:ambito):
        return{ "tipo":"201701015R","valor":self.valor,"fila":self.fila,"columna":self.columna}
    
    def traducir(self,arbol:Arbol, tabla):
        pass