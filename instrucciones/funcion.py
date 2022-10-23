from ast import Nonlocal
from expresion.Tipo import Tipo
from instrucciones.declarar import declarar
from instrucciones.declararArray import declararArray
from instrucciones.instrucciones import instrucciones
from simbolo.arbol import Arbol

class funcion(instrucciones):
    
    def __init__(self, fila, columna,id,tipo, contenido,parametros):
        self.fila =fila
        self.columna = columna
        self.id = id
        self.tipo = tipo
        self.contenido = contenido
        self.parametros=parametros
        
    
    def ejecutar(self,ambito):
        ambito.nuevaFuncion(self)
    
    def traducir(self,arbol:Arbol, tabla):
        arbol.getFunciones().append(self)
        codigo = ""
        aux = ""
        lSalida = arbol.newLabel()
        tabla.masTamanio()
        if self.id == "main":
            codigo += "int " + self.id+"() {\n"
        else:
            codigo += "void " + self.id+"() {\n"
        nRetorno = arbol.newTemp()
        codigo += arbol.assigTemp1(nRetorno["temporal"], "P")
        for nuevoVal in range(len(self.parametros)):
            if isinstance(self.parametros[nuevoVal],str):
                t= declararArray(self.fila,self.columna,self.parametros[nuevoVal],Tipo.ENTERO,[],True,[])
                self.parametros[nuevoVal]=t
                tmpsNoUsados = arbol.getTempNoUsados()
                nuevaDec = t.traducir(arbol, tabla)
                arbol.setTempNoUsados(tmpsNoUsados)
            else:
                if self.parametros[nuevoVal].tipo == None:
                    self.parametros[nuevoVal].tipo = Tipo.ENTERO
                tmpsNoUsados = arbol.getTempNoUsados()
                #print(tmpsNoUsados)
                nuevaDec = self.parametros[nuevoVal].traducir(arbol, tabla)
                arbol.setTempNoUsados(tmpsNoUsados)
        transferencia = {"break":None,"continue":None,"return":lSalida,"temporal":nRetorno["temporal"]}
        aux = self.contenido.traducir(arbol, tabla,condi=transferencia)
        codigo += aux["codigo"]
        codigo += arbol.goto(lSalida)
        codigo += arbol.getLabel(lSalida)
        if self.id == "main":
            codigo += "return 0;\n}\n"
        else:
            codigo += "return;\n}\n"
        arbol.tamReturn = 0
        if self.tipo is None:
            self.tipo=aux["tipo"]
        return {'codigo': codigo}
