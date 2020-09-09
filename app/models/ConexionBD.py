from flask_mysqldb import MySQL

class ConexionBD:

    def __init__(self):
        self._db = MySQL()

    def config(self,app):
        self._db.init_app(app)

    def getCursor(self):
        return self._db.connection.cursor()

    def getDB(self):
        return self._db