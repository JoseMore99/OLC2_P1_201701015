from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol

class While(instrucciones):
    
    def __init__(self, fila, columna,condicion,contenido):
        self.fila =fila
        self.comlumna = columna
        self.condicion = condicion
        self.contenido = contenido
        
    
    def ejecutar(self,ambito:ambito):
        auxcondi = self.condicion.ejecutar(ambito)
        if(auxcondi["tipo"]==Tipo.BOOL):
            while(auxcondi["valor"]):
                respuesta = self.contenido.ejecutar(ambito)
                if(respuesta is not None):
                    if(respuesta["tipo"]=="201701015B"):
                        break
                    if(respuesta["tipo"]=="201701015C"):
                        continue
                    if(respuesta["tipo"]=="201701015R"):
                            return respuesta
                auxcondi = self.condicion.ejecutar(ambito)
            #return respuesta
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "condicion incorrecta en while")

    def traducir(self,arbol:Arbol, tabla):
        pass