
from expresion.Tipo import Tipo
from expresion.expresion import expresion
from simbolo.arbol import Arbol
import simbolo.listaerrores as errores
class aritmetica(expresion):

    def __init__(self, fila, columna,izquierda,derecha, tipoArit):
        self.fila = fila
        self.columna = columna
        self.izquierda=izquierda
        self.derecha=derecha
        self.tipoArit = tipoArit

    def ejecutar(self,ambito):
        valIz = self.izquierda.ejecutar(ambito)
        valDer = self.derecha.ejecutar(ambito)
        #print(str(valIz["tipo"])+"+"+str(valDer["tipo"]))
        if(valIz["tipo"]==valDer["tipo"]):
            if self.tipoArit == "+"  : 
                return {"valor": valIz["valor"]+valDer["valor"], "tipo": valIz["tipo"]}
            elif self.tipoArit == "-" :
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]-valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "*" :
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]*valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "/" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                    if (valDer["valor"]!=0):
                        return {"valor": valIz["valor"]/valDer["valor"], "tipo": valIz["tipo"]}
                    else:
                        errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Aritmetica incorrecta, Division por cero")
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "%" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]%valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "^" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]**valDer["valor"], "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "r" : 
                #print("RAIIIIIIIIIIIIIIIIIIIIIIIZ")
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": valIz["valor"]**(0.5), "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
            elif self.tipoArit == "a" : 
                if(str(valIz["valor"]).isdigit and str(valDer["valor"]).isdigit):
                     return {"valor": abs(valIz["valor"]), "tipo": valIz["tipo"]}
                else:
                    errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        temp = arbol.newTemp()
        izq = der = uno = None
        izq = self.izquierda.traducir(arbol, tabla)
        der = self.derecha.traducir(arbol, tabla)
        if self.tipoArit == "+" :  # FUNCION MAS
            self.ope = "+"
            retorno = self.operador1SumaC3D(izq["temporal"], der["temporal"])
            codigo += izq["codigo"]
            codigo += der["codigo"]
            codigo += arbol.assigTemp2(temp["temporal"],retorno["izquierda"], self.ope, retorno["derecha"])
        elif self.tipoArit == "-" :  # FUNCION MENOS
            self.ope = "-"
            retorno = self.operador1RestaC3D(izq["temporal"], der["temporal"])
            codigo += izq["codigo"]
            codigo += der["codigo"]
            codigo += arbol.assigTemp2(temp["temporal"],
                                       retorno["izquierda"], self.ope, retorno["derecha"])
        elif self.tipoArit == "*" :  # FUNCION POR
            self.ope = "*"
            if self.izquierda.tipo == Tipo.STRING and self.derecha.tipo == Tipo.STRING:
                self.tipo = Tipo.STRING
                retorno = arbol.concatenaString(izq["heap"], der["heap"])
                codigo += izq["codigo"]
                codigo += der["codigo"]
                codigo += retorno["codigo"]
                return {'heap': retorno["heap"], 'codigo': codigo}
            else:
                retorno = self.operador1MultiC3D(
                    izq["temporal"], der["temporal"])
                codigo += izq["codigo"]
                codigo += der["codigo"]
                codigo += arbol.assigTemp2(temp["temporal"],
                                           retorno["izquierda"], self.ope, retorno["derecha"])
        elif self.tipoArit == "%" :  # FUNCION MODULO
            self.ope = "%"
            lTrue = arbol.newLabel()
            lSalida = arbol.newLabel()
            retorno = self.operador1DivisionC3D(
                izq["temporal"], der["temporal"])
            codigo += izq["codigo"]
            codigo += der["codigo"]
            codigo += arbol.getCond2(der["temporal"], " != ", "0.0", lTrue)
            codigo += arbol.imprimir('"%c", 77')  # M
            codigo += arbol.imprimir('"%c", 97')  # a
            codigo += arbol.imprimir('"%c", 116')  # t
            codigo += arbol.imprimir('"%c", 104')  # h
            codigo += arbol.imprimir('"%c", 69')  # E
            codigo += arbol.imprimir('"%c", 114')  # r
            codigo += arbol.imprimir('"%c", 114')  # r
            codigo += arbol.imprimir('"%c", 111')  # o
            codigo += arbol.imprimir('"%c", 114')  # r
            codigo += arbol.assigTemp1(temp["temporal"], "0.0")
            codigo += arbol.goto(lSalida)
            codigo += arbol.getLabel(lTrue)
            arbol.setImports("\"math\"")
            codigo += arbol.assigTempMod(temp["temporal"],
                                         retorno["izquierda"], retorno["derecha"])

            codigo += arbol.getLabel(lSalida)
        elif self.tipoArit == "/" :
            self.ope = "/"
            lTrue = arbol.newLabel()
            lSalida = arbol.newLabel()
            nuevoDer = arbol.newTemp()
            retorno = self.operador1DivisionC3D(
                izq["temporal"], der["temporal"])
            codigo += izq["codigo"]
            codigo += der["codigo"]
            codigo += arbol.getCond2(der["temporal"], " != ", "0.0", lTrue)
            codigo += arbol.imprimir('"%c", 77')  # M
            codigo += arbol.imprimir('"%c", 97')  # a
            codigo += arbol.imprimir('"%c", 116')  # t
            codigo += arbol.imprimir('"%c", 104')  # h
            codigo += arbol.imprimir('"%c", 69')  # E
            codigo += arbol.imprimir('"%c", 114')  # r
            codigo += arbol.imprimir('"%c", 114')  # r
            codigo += arbol.imprimir('"%c", 111')  # o
            codigo += arbol.imprimir('"%c", 114')  # r
            codigo += arbol.assigTemp1(temp["temporal"], "0.0")
            codigo += arbol.goto(lSalida)
            codigo += arbol.getLabel(lTrue)
            codigo += arbol.assigTemp1(nuevoDer["temporal"], retorno["derecha"])
            codigo += arbol.assigTemp2(temp["temporal"],
                                       retorno["izquierda"], self.ope, nuevoDer["temporal"])
            codigo += arbol.getLabel(lSalida)

            '''
            if (t2!=0){goto verdadero};
            print matherror
            t3=0;
            goto salida
            verdadero:
            instruccion
            salida:
            '''
        elif self.tipoArit == "^" :  # PENDIENTES CON DECIMALES
            if self.izquierda.tipo == Tipo.CADENA and self.derecha.tipo == Tipo.ENTERO:
                self.tipo = Tipo.CADENA
                lControl = arbol.newLabel()
                lSalida = arbol.newLabel()
                tempControl = arbol.newTemp()
                codigo += arbol.assigTemp1(
                    tempControl["temporal"], der["temporal"])
                codigo += arbol.getLabel(lControl)
                codigo += arbol.getCond2(tempControl["temporal"],
                                         "<=", "1.0", lSalida)
                dato = arbol.potenciaCadena(izq["heap"],
                                            der["temporal"])
                codigo += arbol.assigTemp2(
                    tempControl["temporal"], tempControl["temporal"], "-", "1.0")
                codigo += arbol.goto(lControl)
                codigo += arbol.getLabel(lSalida)
                codigo += izq["codigo"]
                codigo += der["codigo"]
                codigo += dato["codigo"]
                # print(dato)
                return {'heap': dato["heap"], 'codigo': codigo}

            # Esto por si no es cadena xd
            self.ope = "*"
            lPotencia = arbol.newLabel()
            lSalida = arbol.newLabel()
            lSigue = arbol.newLabel()
            lInicio = arbol.newLabel()
            temp = arbol.newTemp()
            tempT2 = arbol.newTemp()
            retorno = self.operador1PotenciaC3D(
                izq["temporal"], der["temporal"])
            t1 = retorno["izquierda"]
            t2 = retorno["derecha"]
            # codigo += retorno["codigo"]
            # verificar si t2 desde el principio es 0
            # verificar si t2 es 1
            # print(t1, t2, temp)
            codigo += izq["codigo"]
            codigo += der["codigo"]
            codigo += arbol.assigTemp1(tempT2["temporal"], t2)
            codigo += arbol.getCond2(tempT2["temporal"], "!=", "0.0", lInicio)
            codigo += arbol.assigTemp1(temp["temporal"], "1.0")
            codigo += arbol.goto(lSalida)
            codigo += arbol.getLabel(lInicio)
            codigo += arbol.assigTemp1(temp["temporal"], t1)
            codigo += arbol.getLabel(lPotencia)
            codigo += arbol.getCond2(
                tempT2["temporal"], " <= ", "1.0", lSalida)
            codigo += arbol.goto(lSigue)
            codigo += arbol.getLabel(lSigue)
            codigo += arbol.assigTemp2(temp["temporal"],
                                       temp["temporal"], self.ope, t1)
            codigo += arbol.assigTemp2(tempT2["temporal"],
                                       tempT2["temporal"], " - ", "1.0")
            codigo += arbol.goto(lPotencia)
            codigo += arbol.getLabel(lSalida)
            '''
                  verificaciones de arriba
            #     L1:
            #     if int(t1)==0 goto salida
            #     goto sigue
            #     sigue:
            #     t2=t2*t2
            #     int(t1)=int(t1)-1
            #     goto L1
            #     salida:
            #     temp=t2
            #     '''
        return {'temporal': temp["temporal"], 'codigo': codigo}
    # --------------------SUMAC3D--------------------------

    def operador1SumaC3D(self, izq, der):
        derecha = self.derecha.tipo
        if self.izquierda.tipo == Tipo.ENTERO:
            return self.derechaSumaC3D(1, derecha, izq, der)
        elif self.izquierda.tipo == Tipo.DECIMAL:
            return self.derechaSumaC3D(2, derecha, izq, der)

    def derechaSumaC3D(self, numero, derecha, izq, der):
        if numero == 1:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
        elif numero == 2:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}

    # -----------RESTAC3D---------------
    def operador1RestaC3D(self, izq, der):
        derecha = self.derecha.tipo
        if self.izquierda.tipo == Tipo.ENTERO:
            return self.derechaRestaC3D(1, derecha, izq, der)
        elif self.izquierda.tipo == Tipo.DECIMAL:
            return self.derechaRestaC3D(2, derecha, izq, der)

    def derechaRestaC3D(self, numero, derecha, izq, der):
        if numero == 1:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}

        elif numero == 2:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")

        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
    # ----------------------MULTIPLICACIONC3D--------------------------

    def operador1MultiC3D(self, izq, der):
        derecha = self.derecha.tipo
        if self.izquierda.tipo == Tipo.ENTERO:
            return self.derechaMultiC3D(1, derecha, izq, der)
        elif self.izquierda.tipo == Tipo.DECIMAL:
            return self.derechaMultiC3D(2, derecha, izq, der)
        elif self.izquierda.tipo == Tipo.CADENA:
            return self.derechaMultiC3D(4, derecha, izq, der)
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Operador invalido")

    def derechaMultiC3D(self, numero, derecha, izq, der):
        if numero == 1:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        elif numero == 2:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        elif numero == 4:
            if derecha == Tipo.STRING:
                self.tipo = Tipo.STRING
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
    # ------------------- MOD C3D -------------------------

    def operador1ModC3D(self, izq, der):
        derecha = self.derecha.tipo
        if self.izquierda.tipo == Tipo.ENTERO:
            return self.derechaModC3D(1, derecha, izq, der)
        elif self.izquierda.tipo == Tipo.DECIMAL:
            return self.derechaModC3D(2, derecha, izq, der)
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Operador invalido")

    def derechaModC3D(self, numero, derecha, izq, der):
        if numero == 1:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        elif numero == 2:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")

    # ------------------------------ DIVISION C3D -------------------------------------------
    def operador1DivisionC3D(self, izq, der):
        derecha = self.derecha.tipo
        if self.izquierda.tipo == Tipo.ENTERO:
            return self.derechaDivisionC3D(1, derecha, izq, der)
        elif self.izquierda.tipo == Tipo.DECIMAL:
            return self.derechaDivisionC3D(2, derecha, izq, der)
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")

    def derechaDivisionC3D(self, numero, derecha, izq, der):
        if numero == 1:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        elif numero == 2:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
    # ------------------- POTENCIAC3D ----------------------------------

    def operador1PotenciaC3D(self, izq, der):
        derecha = self.derecha.tipo
        if self.izquierda.tipo == Tipo.ENTERO:
            return self.derechaPotenciaC3D(1, derecha, izq, der)
        elif self.izquierda.tipo == Tipo.DECIMAL:
            return self.derechaPotenciaC3D(2, derecha, izq, der)
        # elif self.izquierda.tipo == Tipo.CADENA:  # TODO
        #     self.tipo=Tipo.CADENA
        #     co
            # return self.derechaPotencia(4, derecha, izq, der)
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Operador invalidos")

    def derechaPotenciaC3D(self, numero, derecha, izq, der):
        if numero == 1:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.ENTERO
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        elif numero == 2:
            if derecha == Tipo.ENTERO:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            elif derecha == Tipo.DECIMAL:
                self.tipo = Tipo.DECIMAL
                return {'izquierda': izq, 'derecha': der}
            else:
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        # elif numero == 4:
        #     if derecha == Tipo.ENTERO:
        #         self.tipo = Tipo.CADENA
        #         cadena = ""
        #         cadena+=arb
        #         return cadena
        #     else:
        #         errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Tipos de datos no operables")
        
