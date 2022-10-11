from expresion.Tipo import Tipo
from instrucciones.declarar import declarar
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
        for nuevoVal in self.parametros:
            if nuevoVal.tipo == None:
                nuevoVal.tipo = Tipo.ENTERO
            tmpsNoUsados = arbol.getTempNoUsados()
            #print(nuevoVal.valor)
            nuevaDec = nuevoVal.traducir(arbol, tabla)
            arbol.setTempNoUsados(tmpsNoUsados)
        aux = self.contenido.traducir(arbol, tabla)
        codigo += aux["codigo"]
        codigo += arbol.goto(lSalida)
        codigo += arbol.getLabel(lSalida)
        if self.id == "main":
            codigo += "return 0;\n}\n"
        else:
            codigo += "return;\n}\n"
        arbol.tamReturn = 0
        # print(self.tipo)
        arbol.getFunciones().append(self)
        return {'codigo': codigo}
