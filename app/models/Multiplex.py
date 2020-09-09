class Multiplex:
    def __init__(self, idMultiplex, nombreMultiplex, ubicacion):
        self.idMultiplex= idMultiplex
        self.nombreMultiplex= nombreMultiplex
        self.ubicacion= ubicacion

    def getidMultiplex(self):
        return self.idMultiplex

    def getnombreMultiplex(self):
        return self.nombreMultiplex

    def getubicacion(self):
        return self.ubicacion

    def setidMultiplex(self, idMultiplex):
        self.idMultiplex= idMultiplex

    def setnombreMultiplex(self, nombreMultiplex):
        self.nombreMultiplex= nombreMultiplex

    def setubicacion(self,ubicacion):
        self.ubicacion= ubicacion
