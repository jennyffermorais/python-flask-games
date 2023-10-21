# import sqlite3
from flask import Flask, redirect, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
#app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Substitua pelo servidor SMTP do seu provedor de e-mail.
app.config['MAIL_PORT'] = 465  # Porta do servidor SMTP (587 para TLS, 465 para SSL, 25 para não seguro).
app.config['MAIL_USE_TLS'] = False  # Use TLS (True/False para SSL).
app.config['MAIL_USE_SSL'] = True  # Use SSL (True/False para TLS).
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Seu endereço de e-mail.
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Sua senha de e-mail.

mail = Mail(app)
# Conectar-se ao banco de dados (ou criar um se não existir)
# conn = sqlite3.connect('games.db', check_same_thread=False)

# Criar um cursor
# Um cursor é um objeto que permite que você execute comandos SQL no banco de dados
# cursor = conn.cursor()

# Criar uma tabela
# cursor.execute('''CREATE TABLE IF NOT EXISTS registrants (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id))''')

# REGISTRANTS = {}

SPORTS = [
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")

    if not email:
        return render_template("error.html", message="Missing email")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    #REGISTRANTS[name] = sport

    # Inserir dados
    # cursor.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))

    message = Message("You are registered!", sender=os.getenv('MAIL_USERNAME'), recipients=[email])
    mail.send(message)

    return render_template("success.html")
"""
@app.route("/registrants")
def registrants():
    # Consultar dados
    # registrants = cursor.execute("SELECT * FROM registrants").fetchall()
    print(registrants)
    return render_template("registrants.html", registrants=registrants) # variável do template e variável do select
"""