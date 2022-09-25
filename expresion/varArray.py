from expresion.expresion import expresion
from expresion.nativo import nativo
from simbolo.ambito import ambito
from expresion.Tipo import Tipo
from simbolo.arbol import Arbol

class varArray(expresion):

    def __init__(self, fila, columna, id,pocisiones):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.pocisiones= pocisiones

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        #print(dimensiones)
        def getpos(i):
                aux = self.pocisiones[i].ejecutar(ambito)
                if i==0:
                    return aux["valor"]
                return aux["valor"]+dimensiones[i]*getpos(i-1)
        try:
            return auxSimbolo.valor[getpos(len(dimensiones)-1)]
        except:
            self.pocisiones.append(nativo(0,0,Tipo.ENTERO,0))
            medida = dimensiones[-1]
            return {"tipo":Tipo.ARRAY,"valor":auxSimbolo.valor[getpos(len(dimensiones)-1):(getpos(len(dimensiones)-1)+medida)]}

    def traducir(self,arbol:Arbol, tabla):
        pass

    '''def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        tempVal = self.valor.ejecutar(ambito)
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
            print("error en variable")'''
    
