from . import empleadoRoute
from app.controllers.EmpleadoDao import EmpleadoDao 

empleadoController = EmpleadoDao()

@empleadoRoute.route('/',methods=['GET'])
def getEmpleados():
    return empleadoController.getEmpleados()