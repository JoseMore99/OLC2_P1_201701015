class simboloc3d:
    def __init__(self, tipo, id, temporal, hipStack):
        self.id = id
        self.tipo = tipo
        self.ubicacion = temporal
        self.stck = hipStack
        self.base = []

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

    def setTipo(self, tipo):
        self.tipo = tipo