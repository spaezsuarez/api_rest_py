from . import peliculaRoute
from flask import request
from app.controllers.PeliculaDao import PeliculaDao

peliculaController = PeliculaDao()

@peliculaRoute.route('/', methods = ['GET'])
def getAll():
    return peliculaController.getAllFilms()

@peliculaRoute.route('/get/', methods =  ['GET'])
def get():
    _id = request.args['id'] 
    return peliculaController.getFilm(_id)