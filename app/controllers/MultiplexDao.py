import json

class MultiplexDao:

    def __init__(self,db):
        self._db = db

    def getAll(self):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Multiplex;',())
        lista = json.dumps(cursor.fetchall())
        return lista

    def get(self,_id):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Multiplex WHERE idMultiplex = %s',[_id])
        multiplex = json.dumps(cursor.fetchall())
        return multiplex

    def createMultiplex(self):
        pass

    def deleteMultiplex(self,_id):
        cursor = self._db.getCursor()
        cursor.execute('DELETE FROM Multiplex WHERE idMultiplex = %s',[_id])
        self._db.getDB().connection.commit()    