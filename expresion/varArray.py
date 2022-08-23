from expresion.expresion import expresion
from simbolo.ambito import ambito

class varArray(expresion):

    def __init__(self, fila, columna, id,pocisiones):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.pocisiones= pocisiones

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        if (auxSimbolo!=None):
            temporal=[]
            for i in self.pocisiones:
                auxpos = i.ejecutar(ambito)
                if(len(temporal)==0):
                    print(len(auxSimbolo.valor))
                    temporal=auxSimbolo.valor[auxpos["valor"]]
                else:
                    temporal=temporal[auxpos["valor"]]
            return {"valor": temporal["valor"], "tipo": temporal["tipo"]}
        else:
            print("error en variable")
    
