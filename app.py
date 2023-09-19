import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Conectar-se ao banco de dados (ou criar um se não existir)
conn = sqlite3.connect('games.db', check_same_thread=False)

# Criar um cursor
# Um cursor é um objeto que permite que você execute comandos SQL no banco de dados
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS registrants (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id))''')

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
    name = request.form.get("name")

    if not name:
        return render_template("error.html", message="Missing name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")

    #REGISTRANTS[name] = sport

    # Inserir dados
    cursor.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    # Consultar dados
    registrants = cursor.execute("SELECT * FROM registrants").fetchall()
    print(registrants)
    return render_template("registrants.html", registrants=registrants) # variável do template e variável do select
