from instrucciones.instrucciones import instrucciones
from simbolo.arbol import Arbol

class Struct(instrucciones):
    
    def __init__(self, fila, columna,id,parametros):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.parametros=parametros
        
    
    def ejecutar(self,ambito):
        ambito.nuevaStruct(self)
    
    def traducir(self,arbol:Arbol, tabla):
        pass