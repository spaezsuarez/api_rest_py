from . import multiplexRoute
from app.controllers.MultiplexDao import MultiplexDao
from app.controllers import db
from flask import request

multiplexController = MultiplexDao(db)

@multiplexRoute.route('/',methods=['GET'])
def getAll():
    return 'Este es el get de multiplex'

@multiplexRoute.route('/', methods = ['DELETE'])
def delete():
    _id = request.args['id']
    multiplexController.deleteMultiplex(_id)
    return 'Multiplex {} eliminado de forma exitosa'.format(_id)
