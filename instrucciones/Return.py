from expresion.Tipo import Tipo
from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol

class Return(instrucciones):
    
    def __init__(self, fila, columna,valor=None):
        self.fila =fila
        self.columna = columna
        self.valor = valor
        
    
    def ejecutar(self,ambito:ambito):
        return{ "tipo":"201701015R","valor":self.valor,"fila":self.fila,"columna":self.columna}
    
    def traducir(self,arbol:Arbol, tabla):
        codigo = ""
        if self.valor != None:
            self.valor.eSetTemporal(self.eTemporal())
            valu = self.valor.traducir(arbol, tabla)
            codigo += valu["codigo"]
            self.tipo = self.valor.tipo
            if self.valor.tipo != Tipo.STRING and self.valor.tipo != Tipo.STRUCT and self.valor.tipo != Tipo.ARRAY:
                codigo += arbol.assigStackN(self.eTemporal(),valu["temporal"])
                codigo += arbol.menosStackV(arbol.tamReturn)

                codigo += arbol.goto(self.eReturn())
            else:
                codigo += arbol.assigStackN(self.eTemporal(),valu["heap"])
                codigo += arbol.menosStackV(arbol.tamReturn)
                codigo += arbol.goto(self.eReturn())
        else:
            self.tipo = Tipo.ENTERO
            codigo += arbol.assigStackN(self.eTemporal(), "-50253107246")
            codigo += arbol.goto(self.eReturn())
        if self.valor is not None:
            return {'codigo': codigo, 'tipo': self.valor.tipo}
        return {'codigo': codigo}