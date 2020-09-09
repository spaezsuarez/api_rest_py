class Silla:
    def __init__(self, idSilla, tipo , precio, Sala_idSala, Sala_Multiplex_idMultiplex):
        self.idSilla= idSilla
        self.tipo= tipo
        self.Sala_idSala= Sala_idSala
        self.precio= precio
        self.Sala_Multiplex_idMultiplex=Sala_Multiplex_idMultiplex

    def getididSilla(self):
        return self.idSilla

    def gettipo(self):
        return self.tipo

    def getprecio(self):
        return self.precio

    def getSala_idSalad(self):
        return self.Sala_idSala

    def getSala_Multiplex_idMultiplex(self):
        return self.Sala_Multiplex_idMultiplex

    def setidProducto(self, idSilla):
        self.idSilla= idSilla

    def settipo(self, tipo):
        self.tipo= tipo

    def setcantidad(self, cantidad):
        self.cantidad= cantidad

    def setSala_idSala(self, Sala_idSala):
        self.Sala_idSala= Sala_idSala

    def setSala_Multiplex_idMultiplex(self, Sala_Multiplex_idMultiplex):
        self.Sala_Multiplex_idMultiplex= Sala_Multiplex_idMultiplex