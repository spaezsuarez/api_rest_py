from flask import Flask
from .routes import clienteRoute,empleadoRoute,multiplexRoute,productoRoute,peliculaRoute
from .private.keys import  keys
from .controllers import db

def init_app():
    app = Flask(__name__)

    #Configuracion de la base de datos
    app.config['MYSQL_HOST'] = keys['host']
    app.config['MYSQL_USER'] = keys['user']    
    app.config['MYSQL_PASSWORD'] = keys['password']
    app.config['MYSQL_DB'] = keys['data_base'] 

    db.config(app)

    #Set de los blue prints
    app.register_blueprint(clienteRoute)
    app.register_blueprint(empleadoRoute)
    app.register_blueprint(multiplexRoute)
    app.register_blueprint(productoRoute)
    app.register_blueprint(peliculaRoute)

    return app
