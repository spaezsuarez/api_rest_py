class Cliente:
    def __init__(self, cedula, telefono, nombre, puntos):
        self.cedula= cedula
        self.telefono= telefono
        self.nombre= nombre
        self.puntos= puntos

    def getCedula(self):
        return self.cedula

    def getTelefono(self):
        return self.telefono

    def getNombre(self):
        return self.nombre

    def getPuntos(self):
        return self.puntos

    def setCedula(self, cedula):
        self.cedula= cedula

    def setTelefono(self, telefono):
        self.telefono= telefono

    def setNombre(self, nombre):
        self.nombre= nombre

    def setPuntos(self, puntos):
        self.puntos= puntos