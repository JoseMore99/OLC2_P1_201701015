from instrucciones.instrucciones import instrucciones
from simbolo.arbol import Arbol

class funcion(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, contenido,parametros):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.tipo = tipo
        self.contenido = contenido
        self.parametros=parametros
        
    
    def ejecutar(self,ambito):
        ambito.nuevaFuncion(self)
    
    def traducir(self,arbol:Arbol, tabla):
        pass