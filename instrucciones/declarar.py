from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class declarar(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, valor,mutabilidad):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad= mutabilidad
        
    
    def ejecutar(self,ambito:ambito):
        if(self.tipo!=None):
            if (self.valor !=None):
                auxval = self.valor.ejecutar(ambito)
               # print(str(auxval["tipo"])+"---"+str(self.tipo))
                if (auxval["tipo"]==self.tipo):
                    simboloNew= simbolo(self.tipo,self.id,auxval["valor"],self.mutabilidad,self.fila,self.comlumna)
                    ambito.nuevosimbolo(simboloNew)
                else:
                    print("Error en declarar")
        else:
            auxval = self.valor.ejecutar(ambito)
            simboloNew= simbolo(auxval["tipo"],self.id,auxval["valor"],self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)