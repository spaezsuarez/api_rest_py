import json
from . import db

class ClienteDao:

    def __init__(self):
        self._db = db

    def createClient(self,cedula,telefono,nombreCliente,puntos):
        cursor = self._db.getCursor()
        query = 'INSERT INTO Cliente VALUES(%s,%s,%s,%s);'
        cursor.execute(query,[cedula,telefono,nombreCliente,puntos])
        self._db.getDB().connection.commit()

    def getAllClients(self):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Cliente;',())
        clientes = json.dumps(cursor.fetchall())
        return clientes

    def getClient(self,_id):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Cliente WHERE cedula = %s;',[_id])
        cliente = json.dumps(cursor.fetchall())
        return cliente

    def deleteClient(self,_id):
        cursor = self._db.getCursor()
        query = 'DELETE FROM Cliente WHERE cedula = %s;'
        cursor.execute(query,[_id])
        self._db.getDB().connection.commit()


