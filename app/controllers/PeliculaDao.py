import json
from . import db

class PeliculaDao:

    def __init__(self):
        self._db = db

    def createPelicula(self):
        pass

    def deletePelicula(self,_id):
        cursor = self._db.getCursor()
        cursor.execute('DELETE FROM Pelicula WHERE idPelicula = %s;',[_id])
        self._db.getDB().connection.commit()

    def getAllFilms(self):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Pelicula;',())
        peliculas = json.dumps(cursor.fetchall())
        return peliculas

    def getFilm(self,_id):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Pelicula WHERE idPelicula = %s',[_id])
        pelicula = json.dumps(cursor.fetchall())
        return pelicula
