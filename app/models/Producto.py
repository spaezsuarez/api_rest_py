class Producto:
    def __init__(self, idProducto, nombreProducto, cantidad, precio):
        self.idProducto= idProducto
        self.nombreProducto= nombreProducto
        self.cantidad= cantidad
        self.precio= precio

    def getidProducto(self):
        return self.idProducto

    def getnombreProducto(self):
        return self.nombreProducto

    def getprecio(self):
        return self.precio

    def getcantidad(self):
        return self.cantidad

    def setidProducto(self, idProducto):
        self.idProducto= idProducto

    def setnombreProducto(self, nombreProducto):
        self.nombreProducto= nombreProducto

    def setcantidad(self, cantidad):
        self.cantidad= cantidad

    def setprecio(self, precio):
        self.precio= precio