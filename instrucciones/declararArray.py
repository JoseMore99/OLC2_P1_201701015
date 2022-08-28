import re
from xml.dom.minidom import DOMImplementation
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class declararArray(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, valor,mutabilidad,dimensiones):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad= mutabilidad
        self.dimensiones=dimensiones
        
    
    def ejecutar(self,ambito:ambito):
        #[[[i64;3],2],2]
        if self.dimensiones ==[]:
           self.ObtenerDimen(self.valor)
        else:
            temp=[]
            for i in self.dimensiones:
                x = i.ejecutar(ambito)
                temp.append(x["valor"])
            self.dimensiones=temp[::-1]
        if(self.tipo!=None):
            retorno=self.recorrer(self.valor,ambito)
            print(retorno)
            simboloNew= simbolo({"tipo":self.tipo,"dimen":self.dimensiones},self.id,retorno,self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)
        else:
            retorno=self.recorrer(self.valor,ambito)
            #print(len(retorno))
            simboloNew= simbolo({"tipo":self.tipo,"dimen":self.dimensiones},self.id,retorno,self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)

    def recorrer(self,array,ambito,tipo=None):
        temp = []
        for i in array:
            if(isinstance(i,list)):
                t=self.recorrer(i,ambito)

                temp.extend(t)
            else: 
                try:
                    self.tipo=i["tipo"]
                    temp.extend(i)
                except:
                    temp.append(i.ejecutar(ambito))
        #print(temp)
        return temp

    def ObtenerDimen(self,array):
        i= array
        if(isinstance(i,list)):
            self.dimensiones.append(len(i))
            self.ObtenerDimen(i[0])
        else:
            return 