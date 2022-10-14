from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.simbolo import simbolo
from simbolo.simboloc3d import simboloc3d

class asignar(instrucciones):
    
    def __init__(self, fila, columna,id,valor):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.valor = valor
        
    
    def ejecutar(self,ambito:ambito):
        auxval = self.valor.ejecutar(ambito)
        simbolo_enc= ambito.buscarsimbolo(self.id)
        #print(simbolo_enc.nombre+str(simbolo_enc.valor))
        if( simbolo_enc.mutabilidad):
            if (simbolo_enc.tipo==auxval["tipo"]):
                simboloNew= simbolo(auxval["tipo"],self.id,auxval["valor"],simbolo_enc.mutabilidad,self.fila,self.comlumna)
                ambito.editarSimbolo(self.id,simboloNew)
            else:
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Tipo incorrecto en asignacion")
        else: 
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Asignacion a variable inmutable")

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
        if variable == None:
            val = self.valor.traducir(arbol, tabla)
            # print(val)
            codigo += val["codigo"]
            if self.valor.tipo != Tipo.STRING and self.valor.tipo != Tipo.STRUCT and self.valor.tipo != Tipo.ARRAY:
                tVar = arbol.newTemp()
                tStck = arbol.newTemp()
                codigo += arbol.assigTemp1(tVar["temporal"],
                                           val["temporal"])
                codigo += arbol.assigTemp2(tStck["temporal"],
                                           "P", "+", tabla.getTamanio())
                codigo += arbol.assigStackN(tStck["temporal"],
                                            tVar["temporal"])
                nuevaVal = simboloc3d(
                    self.valor.tipo, self.id,  tabla.getTamanio(), True)
                tabla.setVariable(nuevaVal)
            else:
                tVar = arbol.newTemp()
                tStck = arbol.newTemp()
                codigo += arbol.assigTemp1(tVar["temporal"], val["heap"])
                codigo += arbol.assigTemp2(tStck["temporal"],
                                           "P", "+", tabla.getTamanio())
                codigo += arbol.assigStackN(tStck["temporal"],
                                            tVar["temporal"])
                nuevaVal = simboloc3d(
                    self.valor.tipo, self.id,  tabla.getTamanio(), False,variable.mutabilidad)
                tabla.setVariable(nuevaVal)
            self.tipo = self.valor.tipo
            return {'codigo': codigo}

        # if not arbol.actualizarTabla(self.id, variable.valor, self.linea, tabla.getNombre(), self.columna):
        #     nuevoSim = ReporteTabla(self.id, variable.valor, 'Variable', str(
        #         self.tipo), tabla.getNombre(), self.linea, self.columna)
        #     arbol.getSimbolos().append(nuevoSim)
        # print(variable.tipo)
        if variable.tipo != Tipo.STRING and variable.tipo != Tipo.STRUCT and variable.tipo != Tipo.ARRAY:
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
            codigo += val["codigo"]
            tVar = arbol.newTemp()

            codigo += arbol.assigTemp1(tVar["temporal"],
                                       val["temporal"])
            codigo += arbol.assigStackN(temp["temporal"],
                                        tVar["temporal"])
            nuevaVal = simboloc3d(
                self.valor.tipo, self.id, variable.getUbicacion(), True,variable.mutabilidad)
            tabla.updateVariable(nuevaVal)
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
            print(self.tipo)
            codigo += val["codigo"]
            tVar = arbol.newTemp()
            # codigo += arbol.assigTemp1(tVar["temporal"], val["heap"])
            #         codigo += arbol.assigTemp2(tStck["temporal"],
            #                                    "P", "+", tabla.getTamanio())
            #         codigo += arbol.assigStackN(tStck["temporal"],
            #                                     tVar["temporal"])
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
            # t1=stack[variable.temporal] devuelve el apuntador del heap
            # return {heap:t1}
