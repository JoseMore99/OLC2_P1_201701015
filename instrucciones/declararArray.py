import re
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class declararArray(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, valor,mutabilidad):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad= mutabilidad
        
    
    def ejecutar(self,ambito:ambito):
        if(self.tipo!=None):
            retorno=self.recorrer(self.valor,ambito)
            print(len(retorno))
            simboloNew= simbolo(self.tipo,self.id,retorno,self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)
        else:
            retorno=self.recorrer(self.valor,ambito)
            print(len(retorno))
            simboloNew= simbolo(self.tipo,self.id,retorno,self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)

    def recorrer(self,array,ambito,tipo=None):
        temp = []
        for i in array:
            if(isinstance(i,list)):
                t=self.recorrer(i,ambito)
                temp.append(t)
            else: 
                temp.append(i.ejecutar(ambito))
        print(temp)
        return temp
            