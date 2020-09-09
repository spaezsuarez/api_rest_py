import json 
from . import db

class EmpleadoDao:

    def __init__(self):
        self._db = db

    def getEmpleados(self):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Empleado;',())
        empleados = json.dumps(cursor.fetchall())
        return empleados

    def getEmpleado(self,_id):
        cursor = self._db.getCursor()
        cursor.execute('SELECT * FROM Empleado WHERE idEmpleado = %s',[_id])
        empleado = json.dumps(cursor.fetchall())
        return empleado

    def addEmpleado(self):
        cursor = self._db.getCursor()
        query = 'INSERT INTO Empleado VALUES(%s,%s,%s,%s,%s)'
        params = []
        cursor.execute(query,params)
        self._db.getDB().connection.commit()

    def deleteEmpleado(self,_id):
        cursor = self._db.getCursor()
        query = 'DELETE FROM Empleado WHERE idEmpleado = %s'
        cursor.execute(query,[_id])
        self._db.getDB().connection.commit()
