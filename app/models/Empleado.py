class Empleado:
    def __init__(self, idEmpleado, cedula , nombre, fechaInicio,idMultiplex,Multiplex_idMultiplex,salario):
        self.idEmpleado= idEmpleado
        self.cedula= cedula
        self.nombre= nombre
        self.fechaInicio=fechaInicio
        self.idMultiplex = idMultiplex
        self.Multiplex_idMultiplex = Multiplex_idMultiplex
        self.salario= salario

    def getidEmpleado(self):
        return self.idEmpleado

    def getcedula(self):
        return self.cedula

    def getnombre(self):
        return self.nombre

    def getfechaInicio(self):
        return self.fechaInicio

    def getidMultiplex(self):
        return self.idMultiplex

    def getSMultiplex_idMultiplexd(self):
        return self.Multiplex_idMultiplex

    def getidsalario(self):
        return self.salario

    def setidEmpleado(self, idEmpleado):
        self.idEmpleado= idEmpleado

    def setcedula(self, cedula):
        self.cedula= cedula

    def setnombre(self, nombre):
        self.nombre= nombre

    def setfechaInicio(self, fechaInicio):
        self.fechaInicio= fechaInicio

    def setidMultiplex(self, idMultiplex):
        self.idMultiplex= idMultiplex

    def setMultiplex_idMultiplex(self, Multiplex_idMultiplex):
        self.Multiplex_idMultiplex= Multiplex_idMultiplex

    def setsalario(self, salario):
        self.salario= salario