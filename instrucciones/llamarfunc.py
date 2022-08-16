
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
            if(len(self.parametros)==len(auxfuncion.parametros)):
                entornoAnt= ambito(Ambito)
                for p in range(len(self.parametros)):
                    auxpara = self.parametros[p].ejecutar(Ambito)
                    auxfunc = auxfuncion.parametros[p]
                    if (auxpara["tipo"]==auxfunc.tipo):
                        auxfunc.valor = self.parametros[p]
                        auxfunc.ejecutar(entornoAnt)
                    else:
                        print("Error en asignacion de parametroes")
                auxfuncion.contenido.ejecutar(entornoAnt)
            else:
                print("Error en parametros de llamar funcion")
        else:
            print("error en llamar funcion")
    
