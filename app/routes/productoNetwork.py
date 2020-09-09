from . import productoRoute

@productoRoute.route('/',methods=['GET'])
def getAll():
    return 'Este es el get de productos'