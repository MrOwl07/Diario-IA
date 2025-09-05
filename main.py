# Importar
import os
from flask import Flask, render_template,request, redirect, session
# Conectando a la biblioteca de bases de datos
from flask_sqlalchemy import SQLAlchemy
import speech

app = Flask(__name__)
app.secret_key = os.urandom(24)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creando una base de datos
db = SQLAlchemy(app)
# Creación de una tabla

class Card(db.Model):
    # Creación de columnas
    # id
    id = db.Column(db.Integer, primary_key=True)
    # Título
    title = db.Column(db.String(100), nullable=False)
    # Descripción
    subtitle = db.Column(db.String(300), nullable=False)
    # Texto
    text = db.Column(db.Text, nullable=False)

    # Salida del objeto y del id
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Asignación #2. Crear la tabla Usuario
class User(db.Model):
    #id
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    #iniio de sesion
    login = db.Column(db.String(100), nullable=False)
    #contrasenia
    password = db.Column(db.String(30), nullable=False)


# Ejecutar la página de contenidos
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Asignación #4. Aplicar la autorización
            user_db = User.query.all()
            for user in user_db:
                if form_login == user.login and form_password == user.password:
                    return redirect('/index')
            else:
                error = 'Nombre de usuario o contraseña incorrectos'
                return render_template('login.html', error = error)

            
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login= request.form['email']
        password = request.form['password']
        
        #Asignación #3. Hacer que los datos del usuario se registren en la base de datos.
        user = User(login = login, password = password)

        db.session.add(user)
        db.session.commit()    
        return redirect('/')
    
    else:    
        return render_template('registration.html')


# Ejecutar la página de contenidos
@app.route('/index')
def index():
    # Visualización de las entradas de la base de datos
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

# Ejecutar la página con la entrada
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)
    return render_template('card.html', card=card)

# Ejecutar la página de creación de entradas
@app.route('/create')
def create():
    return render_template('create_card.html')

@app.route('/voice', methods=['POST'])
def voices():
    # Recuperar lo que ya estaba escrito en el textarea
    current_text = request.form.get('text', '')
    
    try:
        voice_text = speech.speech_es()
        # Concatenar el texto escrito + lo nuevo grabado
        session['voice_text'] = current_text + ' ' + voice_text
    except:
        session['voice_text'] = current_text + ' Algo salió mal...'
    
    return render_template('create_card.html', text=session['voice_text'])

# El formulario de inscripción
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Creación de un objeto que se enviará a la base de datos
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')





if __name__ == "__main__":
    app.run(debug=True)