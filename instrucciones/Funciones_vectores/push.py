from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.simbolo import simbolo

class push(instrucciones):
    
    def __init__(self, fila, columna, id,valor):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.valor = valor

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        #print(self.valor)
        if(isinstance(self.valor,list)):

            try:
                auxSimbolo.tipo["dimen"][1]=len(self.valor)
                auxSimbolo.tipo["dimen"][0]+=1
            except:
                auxSimbolo.tipo["dimen"].append(len(self.valor))
            #print(auxSimbolo.tipo["dimen"][0])
            #print(auxSimbolo.tipo["dimen"][1])
            for val in self.valor:
                auxSimbolo.valor.append(val.ejecutar(ambito))
        if len(dimensiones)==1:
            auxSimbolo.tipo["dimen"][0]+=1
            auxSimbolo.valor.append(self.valor.ejecutar(ambito))
            
    def traducir(self,arbol:Arbol, tabla):
        pass