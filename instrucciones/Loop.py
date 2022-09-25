from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol

class Loop(instrucciones):
    
    def __init__(self, fila, columna,contenido):
        self.fila =fila
        self.comlumna = columna
        self.contenido = contenido
        
    
    def ejecutar(self,ambito:ambito):
        while(True):
            respuesta = self.contenido.ejecutar(ambito)
            if(respuesta is not None):
                if(respuesta["tipo"]=="201701015B"):
                    break
                if(respuesta["tipo"]=="201701015C"):
                    continue
                if(respuesta["tipo"]=="201701015R"):
                        return respuesta
    def traducir(self,arbol:Arbol, tabla):
        pass