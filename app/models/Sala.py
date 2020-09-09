class Sala:
    def __init__(self, idSala, Multiplex_idMultiplex):
        self.idSala= idSala
        self.Multiplex_idMultiplex= Multiplex_idMultiplex

    def getididSala(self):
        return self.idSala

    def getnombreMultiplex(self):
        return self.nombreMultiplex

    def setididSala(self, idSala):
        self.idSala= idSala

    def setMultiplex_idMultiplex(self, Multiplex_idMultiplex):
        self.Multiplex_idMultiplex= Multiplex_idMultiplex

