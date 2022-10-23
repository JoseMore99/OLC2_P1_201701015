class simboloc3d:
    def __init__(self, tipo, id, temporal, hipStack,mutabilidad = False):
        self.id = id
        self.tipo = tipo
        self.ubicacion = temporal
        self.stck = hipStack
        self.mutabilidad=mutabilidad
        self.base = []
        self.dimensiones=[]

    def setBase(self, b):
        self.base.append(b)

    def getBase(self, b):
        for i in self.base:
            if i.getIdentificador() == b:
                return i
        return None

    def getMod(self):
        return self.esConst

    def getTipo(self):
        return self.tipo

    def getIdentificador(self):
        return self.id

    def getUbicacion(self):
        return self.ubicacion

    def getDimensiones(self):
        return self.dimensiones

    def setTipo(self, tipo):
        self.tipo = tipo

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def setDimensiones(self, dimensiones):
        self.dimensiones = dimensiones