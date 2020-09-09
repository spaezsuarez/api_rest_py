class Pelicula:
    def __init__(self, idPelicula, nombre, duracion):
        self.idPelicula= idPelicula
        self.nombre= nombre
        self.duracion= duracion

    def getidPelicula(self):
        return self.idPelicula

    def getnombre(self):
        return self.nombre

    def getduracion(self):
        return self.duracion

    def setidPelicula(self,idPelicula):
        self.idPelicula= idPelicula

    def setnombre(self, nombre):
        self.nombre= nombre

    def setduracion(self, duracion):
        self.duracion= duracion
