from abc import ABC, abstractmethod 

class expresion(ABC):
    def __init__(self, fila, columna):
        self.fila =fila
        self.comlumna = columna
        super().__init__()
    
    @abstractmethod
    def ejecutar():
        pass