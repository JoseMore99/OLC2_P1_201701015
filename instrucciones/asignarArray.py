from wsgiref.validate import validator
from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.simbolo import simbolo
from simbolo.simboloc3d import simboloc3d

class asignarArray(instrucciones):
    
    def __init__(self, fila, columna, id,pocisiones,valor):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.pocisiones= pocisiones
        self.valor = valor

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        dimensiones= auxSimbolo.tipo["dimen"]
        #print(dimensiones)
        def getpos(i):
            aux = self.pocisiones[i].ejecutar(ambito)
            if i==0:
                return aux["valor"]
            return aux["valor"]+dimensiones[i]*getpos(i-1)
        auxSimbolo.valor[getpos(len(dimensiones)-1)]=self.valor.ejecutar(ambito)

    def traducir(self,arbol:Arbol, tabla):
        
        codigo = ""
        # TODO cambiar variable con if !=None
        var = tabla.getVariable(self.id)
        variable = None
        cont = 0
        #print(var)
        if var != None:
            variable = var["simbolo"]
            cont = var["entorno"]
        dimensiones= variable.dimensiones
        #print(dimensiones)
        def getpos(i):
                aux = self.pocisiones[i].valor
                if i==0:
                    return aux
                return aux+dimensiones[i]*getpos(i-1)
        if variable.tipo != Tipo.STRING and variable.tipo != Tipo.STRUCT and variable.tipo != Tipo.ARRAY:
            temp = arbol.newTemp()
            tempAcceso = arbol.newTemp()
            codigo += arbol.assigTemp2(tempAcceso["temporal"],"P", "-", cont)
            codigo += arbol.assigTemp2(tempAcceso["temporal"],tempAcceso["temporal"], "+", variable.getUbicacion())
            codigo += arbol.getStack(temp["temporal"], tempAcceso["temporal"])
            # t1=stack[variable.temporal]
            # return {temporal:t1}
            val = self.valor.traducir(arbol, tabla)
            codigo += val["codigo"]
            tVar = arbol.newTemp()
            tPos = arbol.newTemp()

            codigo += arbol.assigTemp2(tPos["temporal"],temp["temporal"], "+", getpos(len(dimensiones)-1))

            codigo += arbol.assigTemp1(tVar["temporal"],val["temporal"])
            codigo += arbol.assigHeap2(tPos["temporal"],  tVar["temporal"])

            nuevaVal = simboloc3d(self.valor.tipo, self.id, variable.getUbicacion(), True,variable.mutabilidad)
            nuevaVal.setDimensiones(dimensiones)
            tabla.setVariable(nuevaVal)
            return {'codigo': codigo}
        else:
            # print(variable.tipo)
            temp = arbol.newTemp()
            tempAcceso = arbol.newTemp()
            codigo += arbol.assigTemp2(tempAcceso["temporal"],
                                       "P", "-", cont)
            codigo += arbol.assigTemp2(tempAcceso["temporal"],
                                       tempAcceso["temporal"], "+", variable.getUbicacion())
            codigo += arbol.assigTemp1(temp["temporal"],
                                       tempAcceso["temporal"])
            # t1=stack[variable.temporal]
            # return {temporal:t1}
            val = self.valor.traducir(arbol, tabla)
            #print(self.tipo)
            codigo += val["codigo"]
            tVar = arbol.newTemp()
            codigo += arbol.assigTemp1(tVar["temporal"],
                                       val["heap"])
            # print(val, "asdasd")
            codigo += arbol.assigStackN(temp["temporal"],
                                        tVar["temporal"])
            nuevaVal = simboloc3d(
                self.valor.tipo, self.id, variable.getUbicacion(), False,variable.mutabilidad)
            tabla.setVariable(nuevaVal)
            self.tipo = variable.tipo
            return {'codigo': codigo}