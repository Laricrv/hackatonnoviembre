from flask import Flask
from modelos import db, Lista

# Instanciar la clase flask 
app = Flask('app')

# Configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#inicializar la base de datos

db.init_app(app)


#crear base de datos
'''
with app.app_context():
    db.create_all()
'''
