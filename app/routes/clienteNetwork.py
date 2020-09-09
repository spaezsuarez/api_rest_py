from . import clienteRoute
from flask import request,Response
from app.controllers.ClienteDao import ClienteDao

clienteController = ClienteDao()

@clienteRoute.route('/',methods=['GET'])
def getAll():
    return clienteController.getAllClients()

@clienteRoute.route('/get/',methods=['GET'])
def getClient():
    _id = request.args['id']
    return clienteController.getClient(_id)

@clienteRoute.route('/create/',methods=['POST'])
def create():
    name = request.json['name']
    phone = request.json['phone']
    points = request.json['points']
    _id = request.args['id']
    clienteController.createClient(_id,phone,name,points)
    return 'Usuario {} creado de forma exitosa'.format(_id)

@clienteRoute.route('/', methods=['DELETE'])
def delete():
    _id = request.args['id']
    clienteController.deleteClient(_id)
    return 'Usuario {} eliminado de forma exitosa'.format(_id)