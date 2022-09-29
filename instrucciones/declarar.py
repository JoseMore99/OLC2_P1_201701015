from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.listasimboloc3d import listasimboloc3d
from simbolo.simbolo import simbolo
from simbolo.simboloc3d import simboloc3d

class declarar(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, valor,mutabilidad):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.tipo = tipo
        self.valor = valor
        self.mutabilidad= mutabilidad
        
    
    def ejecutar(self,ambito:ambito):
        if ambito.existesimbolo(self.id):
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', 'variable declarada dos veces')
        else:
            if(self.tipo!=None):
                if (self.valor !=None):
                    auxval = self.valor.ejecutar(ambito)
                # print(str(auxval["tipo"])+"---"+str(self.tipo))
                    if (auxval["tipo"]==self.tipo):
                        simboloNew= simbolo(self.tipo,self.id,auxval["valor"],self.mutabilidad,self.fila,self.comlumna)
                        ambito.nuevosimbolo(simboloNew)
                    else:
                        import simbolo.listaerrores as errores
                        errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Declaracion de tipo incitrecta")
            else:
                auxval = self.valor.ejecutar(ambito)
                simboloNew= simbolo(auxval["tipo"],self.id,auxval["valor"],self.mutabilidad,self.fila,self.comlumna)
                ambito.nuevosimbolo(simboloNew)

    def traducir(self,arbol:Arbol, tabla:listasimboloc3d):
        codigo = ""
        val = self.valor.traducir(arbol, tabla)
        if self.valor.tipo != self.tipo:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Tipos incompatibles")
        codigo += val["codigo"]
        if tabla.getVariableEntorno(self.id) == None:
            # if not cadena, struct o arreglo:
            if self.valor.tipo != Tipo.STRING and self.valor.tipo != Tipo.STRUCT and self.valor.tipo != Tipo.ARRAY:
                tVar = arbol.newTemp()
                tStck = arbol.newTemp()
                codigo += arbol.assigTemp1(tVar["temporal"],val["temporal"])
                codigo += arbol.assigTemp2(tStck["temporal"],"P", "+", tabla.getTamanio())
                codigo += arbol.assigStackN(tStck["temporal"],tVar["temporal"])
                nuevaVal = simboloc3d(self.tipo, self.id,  tabla.getTamanio(), True)
                tabla.setVariable(nuevaVal)
                
            else:
                tVar = arbol.newTemp()
                tStck = arbol.newTemp()
                codigo += arbol.assigTemp1(tVar["temporal"], val["heap"])
                codigo += arbol.assigTemp2(tStck["temporal"],"P", "+", tabla.getTamanio())
                codigo += arbol.assigStackN(tStck["temporal"],tVar["temporal"])
                nuevaVal = simboloc3d(self.tipo, self.id,  tabla.getTamanio(), False)
                tabla.setVariable(nuevaVal)
            # else: guardar en heap y despues la referencia en stack
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Variable ya existente")

        print("aquiiiiiii")
        print(tabla.getTamanio())
        return {'codigo': codigo}
