from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.arbol import Arbol
from simbolo.simbolo import simbolo

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
        pass
