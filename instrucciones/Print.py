from expresion.Tipo import Tipo
from expresion.expresion import expresion
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
                for i in self.expresiones:
                    # se imprime segun el tipo
                    tempvar = tempvar.replace("{}",str(i.valor),1)
                for j in tempvar:
                    codigo += arbol.imprimir('"%c", (int)'+str(ord(j)))
        
        codigo += arbol.imprimir('"%c", (int)10')
        
        return {'codigo': codigo}
def vaciar():
    global consola
    consola=""