
from expresion.Tipo import Tipo
from expresion.expresion import expresion
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
import simbolo.listaerrores as errores

class variable(expresion):

    def __init__(self, fila, columna, id):
        self.fila = fila
        self.columna = columna
        self.id = id
        self.tipo=Tipo.ENTERO

    def ejecutar(self,ambito:ambito):
        auxSimbolo = ambito.buscarsimbolo(self.id)
        if (auxSimbolo!=None):
            return {"valor": auxSimbolo.valor, "tipo": auxSimbolo.tipo}
        else:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Variable no declarada")

    def traducir(self,arbol:Arbol, tabla):
        codigo = "//variable\n"
        var = tabla.getVariable(self.id)
        print(var)
        if var == None:
            errores.Errores.nuevoError(self.fila,self.columna, 'Semantico', "Variable no declarada")

        variable = var["simbolo"]
        cont = var["entorno"]
        self.tipo = variable.tipo
        # if not arbol.actualizarTabla(self.identificador, variable.valor, self.linea, tabla.getNombre(), self.columna):
        #     nuevoSim = ReporteTabla(self.identificador, variable.valor, 'Variable', str(
        #         self.tipo), tabla.getNombre(), self.linea, self.columna)
        #     arbol.getSimbolos().append(nuevoSim)
       
        if variable.tipo != Tipo.STRING and variable.tipo != Tipo.STRUCT and variable.tipo != Tipo.ARRAY:
            temp = arbol.newTemp()
            tempAcceso = arbol.newTemp()
            codigo += arbol.assigTemp2(tempAcceso["temporal"],
                                       "P", "-", cont)
            codigo += arbol.assigTemp2(tempAcceso["temporal"],
                                       tempAcceso["temporal"], "+", variable.getUbicacion())
            codigo += arbol.getStack(temp["temporal"], tempAcceso["temporal"])
            # t1=stack[variable.temporal]
            # return {temporal:t1}
            return {'temporal': temp["temporal"], 'codigo': codigo}
        else:
            temp = arbol.newTemp()
            tempAcceso = arbol.newTemp()
            codigo += arbol.assigTemp2(tempAcceso["temporal"],
                                       "P", "-", cont)
            codigo += arbol.assigTemp2(tempAcceso["temporal"],
                                       tempAcceso["temporal"], "+", variable.getUbicacion())
            codigo += arbol.getStack(temp["temporal"], tempAcceso["temporal"])
            # t1=stack[variable.temporal] devuelve el apuntador del heap
            # return {heap:t1}
            return {'heap': temp["temporal"], 'codigo': codigo}




