import re
from xml.dom.minidom import DOMImplementation
from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.simbolo import simbolo
from simbolo.simboloc3d import simboloc3d

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
            if self.valor==[]:
                self.dimensiones=[0]
            else:
                self.ObtenerDimen(self.valor)
        else:
            temp=[]
            for i in self.dimensiones:
                x = i.ejecutar(ambito)
                temp.append(x["valor"])
            self.dimensiones=temp[::-1]
        if(self.tipo!=None):
            retorno=self.recorrer(self.valor,ambito)
            #print(retorno)
            simboloNew= simbolo({"tipo":self.tipo,"dimen":self.dimensiones},self.id,retorno,self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)
        else:
            retorno=self.recorrer(self.valor,ambito)
            #print(len(retorno))
            simboloNew= simbolo({"tipo":self.tipo,"dimen":self.dimensiones},self.id,retorno,self.mutabilidad,self.fila,self.comlumna)
            ambito.nuevosimbolo(simboloNew)

    def traducir(self,arbol:Arbol, tabla):
        codigo=""
        if self.dimensiones ==[]:
            if self.valor==[]:
                self.dimensiones=[0]
            else:
                self.ObtenerDimen(self.valor)
        else:
            temp=[]
            for i in self.dimensiones:
                x = i.valor
                temp.append(x)
            self.dimensiones=temp[::-1]
        if tabla.getVariableEntorno(self.id) == None:
            # if not cadena, struct o arreglo:
            retorno=self.recorrerC3D(self.valor)
            val = arbol.guardarArreglo(retorno)

            codigo +=val["codigo"]
            
            tVar = arbol.newTemp()
            tStck = arbol.newTemp()
            codigo += arbol.assigTemp1(tVar["temporal"], val["heap"])
            codigo += arbol.assigTemp2(tStck["temporal"],"P", "+", tabla.getTamanio())
            codigo += arbol.assigStackN(tStck["temporal"],tVar["temporal"])
            nuevaVal = simboloc3d(self.tipo, self.id,  tabla.getTamanio(), False,self.mutabilidad)
            nuevaVal.setDimensiones(self.dimensiones)
            tabla.setVariable(nuevaVal)
            # else: guardar en heap y despues la referencia en stack
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Variable ya existente")

        #print("aquiiiiiii")
        #print(tabla.getTamanio())
        return {'codigo': codigo}

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
    
    def recorrerC3D(self,array):
        temp = []
        for i in array:
            if(isinstance(i,list)):
                t=self.recorrerC3D(i)

                temp.extend(t)
            else: 
                try:
                    self.tipo=i.tipo
                    temp.extend(i)
                except:
                    temp.append(i.valor)
        #print(temp)
        return temp

    def ObtenerDimen(self,array):
        i= array
        if(isinstance(i,list)):
            self.dimensiones.append(len(i))
            self.ObtenerDimen(i[0])
        else:
            return 