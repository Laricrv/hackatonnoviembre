from flask_sqlalchemy import SQLAlchemy

#instanciar sqlalchemy

db = SQLAlchemy()

#crear modelos

class Lista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable = False)
    mes = db.Column(db.String(20))
    tarea1 = db.Column(db.String(200))
    tarea2 = db.Column(db.String(200))
    tarea3 = db.Column(db.String(200))
    tarea4 = db.Column(db.String(200))
    tarea5 = db.Column(db.String(200))
    notas = db.Column(db.String(200))