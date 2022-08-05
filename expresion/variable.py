
from expresion.expresion import expresion
from simbolo.ambito import ambito

class variable(expresion):

    def __init__(self, fila, columna, id):
        self.fila = fila
        self.columna = columna
        self.id = id

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        if (auxSimbolo!=None):
            return {"valor": auxSimbolo.valor, "tipo": auxSimbolo.tipo}
        else:
            print("error en variable")
    




