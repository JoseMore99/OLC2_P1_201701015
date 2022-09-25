from __future__ import barry_as_FLUFL
from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol

class Match(instrucciones):
    
    def __init__(self, fila, columna,condicion,coincidencias):
        self.fila =fila
        self.comlumna = columna
        self.condicion = condicion
        self.coincidencias = coincidencias
        
    
    def ejecutar(self,ambito:ambito):
        auxcondi = self.condicion.ejecutar(ambito)
        bul=True
        for i in self.coincidencias:
            for j in i.listaval:
                try:
                    tempcondi = j.ejecutar(ambito)
                except:
                    if(j=='_' and bul):
                        aux = i.ejecutar(ambito)
                        if aux is not None:
                            return aux
                if(auxcondi["valor"]==tempcondi["valor"] and auxcondi["tipo"]==tempcondi["tipo"] ):
                    bul=False
                    print(auxcondi)
                    print(tempcondi)
                    aux = i.ejecutar(ambito)
                    if aux is not None:
                        return aux
            if not bul:
                break
    def traducir(self,arbol:Arbol, tabla):
        pass
                   
                