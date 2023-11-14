from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Lista


# Instanciar la clase flask 
app = Flask(__name__)

# Configuramos la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar nuestra db 
db.init_app(app)

#Rutas

# Read - Leer

@app.route('/')
def index():
    listas = Lista.query.all()

    return render_template ('index.html', listas=listas)


# Ruta create - crear

@app.route('/crear', methods=['GET','POST'])
def crear():
    if request.method  == 'POST':

        # Obtener los datos de mi formulario
        nombre = request.form.get('nombre')
        mes = request.form.get('mes')
        tarea1 = request.form.get('tarea1')        
        tarea2 = request.form.get('tarea2')
        tarea3 = request.form.get('tarea3')
        tarea4 = request.form.get('tarea4')
        tarea5 = request.form.get('tarea5')
        notas = request.form.get('notas')
        # Creamos el objeto lista
        lista = Lista(nombre=nombre, mes=mes, tarea1=tarea1, tarea2=tarea2, tarea3=tarea3, tarea4=tarea4, tarea5=tarea5, notas=notas)

        # Agregar a la db
        db.session.add(lista)

        # Guardamos los cambios
        db.session.commit()

        return render_template ('crear.html')
    return render_template ('crear.html')


#Ruta Eliminar

@app.route('/eliminar/<id>')
def eliminar(id):
    lista = Lista.query.get_or_404(id)

    db.session.delete(lista)
    db.session.commit()

    return redirect(url_for('home'))

#Ruta Editar

@app.route('/editar/<id>', methods=['GET', 'POST'])
def editar(id):

    lista = Lista.query.get(id)

    if request.method  == 'POST':

        # Obtener los datos de mi formulario
        lista.nombre = request.form.get('nombre')
        lista.mes = request.form.get('mes')
        lista.tarea1 = request.form.get('tarea1')
        lista.tarea2 = request.form.get('tarea2')
        lista.tarea3 = request.form.get('tarea3')
        lista.tarea4 = request.form.get('tarea4')
        lista.notas = request.form.get('notas')

        # Guardamos los cambios
        db.session.commit()

        return redirect (url_for('index'))
    
    return render_template('editar.html', lista=lista)

#Ruta Home

@app.route('/home')
def home():
    listas = Lista.query.all()

    return render_template ('home.html', listas=listas)





### BREAKPOINT ###
if __name__ == '__main__':
    app.run(debug=True, port=5005)