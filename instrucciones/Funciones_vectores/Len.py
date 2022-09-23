
from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class Len(instrucciones):
    
    def __init__(self, fila, columna, id):
        self.fila = fila
        self.columna = columna
        self.id = id

    def ejecutar(self,ambito:ambito):
        if (isinstance(self.id,str)):
            auxSimbolo = ambito.buscarsimbolo(self.id)
            dimensiones= auxSimbolo.tipo["dimen"]
            return {"valor": dimensiones[0], "tipo": Tipo.ENTERO}
        else:
            auxSimbolo = self.id.ejecutar(ambito)
            #print("+++++++++++++")
            #print(auxSimbolo)
            longitud=len(auxSimbolo["valor"])
            #print("Longitud {}".format(longitud))
            return {"valor":longitud, "tipo": Tipo.ENTERO}
        
            