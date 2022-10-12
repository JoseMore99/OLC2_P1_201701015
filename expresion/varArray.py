from expresion.expresion import expresion
from expresion.nativo import nativo
from simbolo.ambito import ambito
from expresion.Tipo import Tipo
from simbolo.arbol import Arbol
import simbolo.listaerrores as errores

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
        codigo = ""
        var = tabla.getVariable(self.id)
        #print(var)
        if var == None:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Variable no declarada")
        variable = var["simbolo"]
        cont = var["entorno"]
        self.tipo = variable.tipo
        dimensiones= variable.dimensiones
        print(dimensiones)
        def getpos(i):
                aux = self.pocisiones[i].valor
                if i==0:
                    return aux
                return aux+dimensiones[i]*getpos(i-1)
        temp = arbol.newTemp()
        tempAcceso = arbol.newTemp()
        codigo += arbol.assigTemp2(tempAcceso["temporal"],"P", "-", cont)
        codigo += arbol.assigTemp2(tempAcceso["temporal"],tempAcceso["temporal"], "+", variable.getUbicacion())
        codigo += arbol.getStack(temp["temporal"], tempAcceso["temporal"])
        tempout= arbol.newTemp()
        tempL= arbol.newTemp()
        codigo += arbol.assigTemp2(tempout["temporal"], temp["temporal"],"+",getpos(len(dimensiones)-1))
        codigo += arbol.getHeap(tempL["temporal"], tempout["temporal"])
        return {'temporal': tempL["temporal"], 'codigo': codigo}

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
    
