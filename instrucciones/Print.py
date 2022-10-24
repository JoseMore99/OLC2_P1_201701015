from expresion.Tipo import Tipo
from expresion.expresion import expresion
from expresion.varArray import varArray
from instrucciones.instrucciones import instrucciones
from simbolo.arbol import Arbol

consola =""
class Print(instrucciones):
    
    def __init__(self, fila, columna, valor, expresiones):
        self.fila =fila
        self.columna = columna
        self.valor = valor
        self.expresiones = expresiones
        
    
    def ejecutar(self,ambito):
        global consola
        aux = self.valor.ejecutar(ambito)
        if(aux!=None and aux["tipo"]==Tipo.STRING):
            if(self.expresiones==[]):
                consola += str(aux["valor"])+"\n"
            else:
                texto = str(aux["valor"])
                for i in self.expresiones:
                    temp = i.ejecutar(ambito)
                    if(temp!=None):
                        #print(temp)
                        if(isinstance(temp["valor"],list)):
                            contenido ="["
                            for j in temp["valor"]:
                                contenido+=str(j["valor"])+","
                            contenido+="]"
                            contenido= contenido.replace(",]","]")
                            texto = texto.replace("{:?}",contenido,1)
                            #print(texto)
                        else:
                            texto = texto.replace("{}",str(temp["valor"]),1)
                        #print(temp["valor"],"-")
                    else:
                        print("Error en replace del print")
                consola+=texto+"\n"
        else:
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error en print")
        #print(consola)

    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        if(self.expresiones==[]):
            variable = self.valor.traducir(arbol, tabla)
            if variable == None:
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error en print")
            # se imprime segun el tipo
            elif self.valor.tipo == Tipo.STRING:
                tempo = arbol.newTemp()
                codigo += variable["codigo"]
                indice = variable["heap"]
                tempL = arbol.newTemp()
                loop = arbol.newLabel()
                lSalida = arbol.newLabel()
                impresion = arbol.newLabel()
                codigo += arbol.assigTemp1(tempo["temporal"], indice)
                #print(codigo)
                codigo += arbol.getHeap(tempL["temporal"], tempo["temporal"])
                codigo += arbol.goto(loop)
                codigo += arbol.getLabel(loop)
                codigo += arbol.getHeap(tempL["temporal"], tempo["temporal"])
                codigo += arbol.getCond2(tempL["temporal"],"==", "-1.0", lSalida)
                codigo += arbol.getCond2(tempL["temporal"],"==", "0.0", impresion)
                codigo += arbol.imprimir('"%c", (int){}'.format(tempL["temporal"]))
                codigo += arbol.getLabel(impresion)
                codigo += arbol.assigTemp2(tempo["temporal"],
                                           tempo["temporal"], "+", "1.0")
                codigo += arbol.goto(loop)
                codigo += arbol.getLabel(lSalida)
            else:
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error en print")
            arbol.setImports(tempo["temporal"])
            arbol.setImports(tempL["temporal"])
        else:
            variable = self.valor.traducir(arbol, tabla)
            if variable == None:
                import simbolo.listaerrores as errores
                errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Error en print")
            elif self.valor.tipo == Tipo.STRING:
                tempvar = self.valor.valor
                contador =0
                for i in self.expresiones:
                    tempvar = tempvar.replace("{}","{")
                    tempvar = tempvar.replace("{:?}","}")
                for j in tempvar:
                    if (j =="{"):
                        temporal= self.expresiones[contador].traducir(arbol, tabla)
                        valor = self.expresiones[contador]
                        #print("-------------------")
                        #print(temporal)
                        #print(valor.tipo)
                        if "temporal"in temporal:
                            if valor.tipo == Tipo.ENTERO:
                                codigo += temporal["codigo"]
                                codigo += arbol.imprimir(
                                    '"%d", (int){}'.format(temporal["temporal"]))
                                #Printf("%d", int(expresion))
                            elif valor.tipo == Tipo.DECIMAL:
                                codigo += temporal["codigo"]
                                codigo += arbol.imprimir(
                                    '"%f", {}'.format(temporal["temporal"]))
                                # Printf("%f", 32.2)
                            elif valor.tipo == Tipo.CHAR:
                                codigo += temporal["codigo"]
                                codigo += arbol.imprimir(
                                    '"%c", {}'.format(temporal["temporal"]))
                                # Printf("%c", 36)
                            elif valor.tipo == Tipo.BOOL:
                                codigo += temporal["codigo"]
                                temp = arbol.newTemp()
                                lTrue = arbol.newLabel()
                                lFalse = arbol.newLabel()
                                lSalida = arbol.newLabel()
                                codigo += arbol.assigTemp1(temp["temporal"],
                                                        temporal["temporal"])
                                codigo += arbol.getCond2(temp["temporal"],
                                                        " == ", "1.0", lTrue)
                                codigo += arbol.goto(lFalse)
                                codigo += arbol.getLabel(lTrue)
                                codigo += arbol.imprimir('"%c", 116')  # t
                                codigo += arbol.imprimir('"%c", 114')  # r
                                codigo += arbol.imprimir('"%c", 117')  # u
                                codigo += arbol.imprimir('"%c", 101')  # e
                                codigo += arbol.goto(lSalida)
                                codigo += arbol.getLabel(lFalse)
                                codigo += arbol.imprimir('"%c", 102')  # f
                                codigo += arbol.imprimir('"%c", 97')  # a
                                codigo += arbol.imprimir('"%c", 108')  # l
                                codigo += arbol.imprimir('"%c", 115')  # s
                                codigo += arbol.imprimir('"%c", 101')  # e
                                codigo += arbol.getLabel(lSalida)
                                '''
                                t1=temporal
                                if(t1==1.0){goto true}
                                goto false
                                true:
                                imprimir(true) caracter por caracter
                                goto salida
                                false:
                                imprimir(false) caracter por caracter
                                salida:
                                '''
                        elif "heap"in temporal:
                            if valor.tipo == Tipo.ENTERO:
                                codigo += temporal["codigo"]
                                codigo += arbol.imprimir(
                                    '"%d", (int){}'.format(temporal["heap"]))
                                #Printf("%d", int(expresion))
                            elif valor.tipo == Tipo.DECIMAL:
                                codigo += temporal["codigo"]
                                codigo += arbol.imprimir(
                                    '"%f", {}'.format(temporal["heap"]))
                                # Printf("%f", 32.2)
                            elif valor.tipo == Tipo.CHAR:
                                codigo += temporal["codigo"]
                                codigo += arbol.imprimir(
                                    '"%c", {}'.format(temporal["heap"]))
                                # Printf("%c", 36)
                            elif valor.tipo == Tipo.BOOL:
                                codigo += temporal["codigo"]
                                temp = arbol.newTemp()
                                lTrue = arbol.newLabel()
                                lFalse = arbol.newLabel()
                                lSalida = arbol.newLabel()
                                codigo += arbol.assigTemp1(temp["heap"],
                                                        temporal["heap"])
                                codigo += arbol.getCond2(temp["heap"],
                                                        " == ", "1.0", lTrue)
                                codigo += arbol.goto(lFalse)
                                codigo += arbol.getLabel(lTrue)
                                codigo += arbol.imprimir('"%c", 116')  # t
                                codigo += arbol.imprimir('"%c", 114')  # r
                                codigo += arbol.imprimir('"%c", 117')  # u
                                codigo += arbol.imprimir('"%c", 101')  # e
                                codigo += arbol.goto(lSalida)
                                codigo += arbol.getLabel(lFalse)
                                codigo += arbol.imprimir('"%c", 102')  # f
                                codigo += arbol.imprimir('"%c", 97')  # a
                                codigo += arbol.imprimir('"%c", 108')  # l
                                codigo += arbol.imprimir('"%c", 115')  # s
                                codigo += arbol.imprimir('"%c", 101')  # e
                                codigo += arbol.getLabel(lSalida)
                                '''
                                t1=temporal
                                if(t1==1.0){goto true}
                                goto false
                                true:
                                imprimir(true) caracter por caracter
                                goto salida
                                false:
                                imprimir(false) caracter por caracter
                                salida:
                                '''
                        contador+=1
                    elif (j=="}"):
                        #equivale a que espera un Vector
                        try:
                            temporal= self.expresiones[contador].traducir(arbol, tabla)
                            codigo+=temporal["codigo"]
                            tempCuenta = arbol.newTemp()
                            tempL = arbol.newTemp()
                            #print(temporal)
                            codigo += arbol.assigTemp1(tempCuenta["temporal"], temporal["pocision"])
                        except:
                            var = tabla.getVariable(self.expresiones[contador].id)
                            variable = var["simbolo"]
                            tempor = varArray(self.expresiones[contador].fila,self.expresiones[contador].columna,variable.id,variable.dimensiones)
                            temporal =tempor.traducir(arbol, tabla)
                            codigo+=temporal["codigo"]
                            tempCuenta = arbol.newTemp()
                            tempL = arbol.newTemp()
                            #print(temporal)
                            codigo += arbol.assigTemp1(tempCuenta["temporal"], temporal["pocision"])
                        codigo += arbol.imprimir('"%c", (int)91')#[
                        tipoimp=""
                        #print(temporal["tipo"])
                        if temporal["tipo"]==Tipo.ENTERO:
                            tipoimp="%d"
                        elif temporal["tipo"]==Tipo.DECIMAL:
                            tipoimp="%f"
                        elif temporal["tipo"]==Tipo.CHAR:
                            tipoimp="%c"
                        for i in range(temporal["medida"]):
                            codigo += arbol.getHeap(tempL["temporal"], tempCuenta["temporal"])
                            codigo += arbol.imprimir('"{}", (int){}'.format(tipoimp,tempL["temporal"]))
                            if i !=temporal["medida"]-1:
                                codigo += arbol.imprimir('"%c", (int)44')#,
                            codigo += arbol.assigTemp2(tempCuenta["temporal"],tempCuenta["temporal"], "+", "1.0")
                        codigo += arbol.imprimir('"%c", (int)93')#]
                        
                    else:
                        codigo += arbol.imprimir('"%c", (int)'+str(ord(j)))
        
        codigo += arbol.imprimir('"%c", (int)10')
        
        return {'codigo': codigo}
def vaciar():
    global consola
    consola=""