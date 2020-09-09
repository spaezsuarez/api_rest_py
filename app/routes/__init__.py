from flask import Blueprint

clienteRoute = Blueprint('cliente',__name__,url_prefix = '/cliente')
empleadoRoute = Blueprint('empleado',__name__,url_prefix = '/empleado')
multiplexRoute = Blueprint('multiplex',__name__,url_prefix = '/multiplex')
productoRoute = Blueprint('producto',__name__,url_prefix = '/producto')
peliculaRoute = Blueprint('pelicula',__name__,url_prefix = '/pelicula')
            
from . import clienteNetwork
from . import empleadoNetwork
from . import multiplexNetwork
from . import productoNetwork
from . import peliculaNetwork