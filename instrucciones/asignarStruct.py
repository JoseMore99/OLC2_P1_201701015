from instrucciones.instrucciones import instrucciones
from simbolo.ambito import ambito
from simbolo.simbolo import simbolo

class asignarStruct(instrucciones):
    
    def __init__(self, fila, columna,id,idstruct,valor):
        self.fila =fila
        self.comlumna = columna
        self.id = id
        self.idstruct = idstruct
        self.valor = valor
        
    
    def ejecutar(self,ambito:ambito):
        auxval = self.valor.ejecutar(ambito)
        simbolo_enc= ambito.buscarsimbolo(self.id)
        #print(simbolo_enc.nombre+str(simbolo_enc.valor))
        if( simbolo_enc.mutabilidad):
            simbolo_enc.valor[self.idstruct]=auxval
            simboloNew= simbolo(simbolo_enc.tipo,self.id,simbolo_enc.valor,simbolo_enc.mutabilidad,self.fila,self.comlumna)
            ambito.editarSimbolo(self.id,simboloNew)
        else: 
            import simbolo.listaerrores as errores
            errores.Errores.nuevoError(self.fila,self.comlumna, 'Semantico', "Asignacion a variable inmutable")
