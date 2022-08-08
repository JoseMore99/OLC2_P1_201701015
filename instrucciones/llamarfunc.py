
from expresion.expresion import expresion
from simbolo.ambito import ambito

class llamarfunc(expresion):

    def __init__(self, fila, columna, id,parametros):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.parametros = parametros

    def ejecutar(self,Ambito:ambito):
        auxfuncion = Ambito.buscarFuncion(self.id)
        if (auxfuncion!=None):
            entornoAnt= ambito(Ambito)
            auxfuncion.contenido.ejecutar(entornoAnt)
        else:
            print("error en llamar funcion")
    
