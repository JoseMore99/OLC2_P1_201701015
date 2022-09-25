from expresion.Tipo import Tipo
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
            if self.valor.tipo == Tipo.ENTERO:
                codigo += variable["codigo"]
                codigo += arbol.imprimir(
                    '"%d", (int){}'.format(variable["temporal"]))
                #Printf("%d", int(expresion))
            elif self.valor.tipo == Tipo.DECIMAL:
                codigo += variable["codigo"]
                codigo += arbol.imprimir(
                    '"%f", {}'.format(variable["temporal"]))
                # Printf("%f", 32.2)
            elif self.valor.tipo == Tipo.CHAR:
                codigo += variable["codigo"]
                codigo += arbol.imprimir(
                    '"%c", {}'.format(variable["temporal"]))
                # Printf("%c", 36)
            elif self.valor.tipo == Tipo.BOOL:
                codigo += variable["codigo"]
                temp = arbol.newTemp()
                lTrue = arbol.newLabel()
                lFalse = arbol.newLabel()
                lSalida = arbol.newLabel()
                codigo += arbol.assigTemp1(temp["temporal"],variable["temporal"])
                codigo += arbol.getCond2(temp["temporal"]," == ", "1.0", lTrue)
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
            elif self.valor.tipo == Tipo.STRING:
                tempo = arbol.newTemp()
                codigo += variable["codigo"]
                indice = variable["heap"]
                tempL = arbol.newTemp()
                loop = arbol.newLabel()
                lSalida = arbol.newLabel()
                impresion = arbol.newLabel()
                codigo += arbol.assigTemp1(tempo["temporal"], indice)
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
        codigo += arbol.imprimir('"%c", (int)10')
        arbol.setImports("\"fmt\"")
        return {'codigo': codigo}
def vaciar():
    global consola
    consola=""