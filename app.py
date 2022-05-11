from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Aula top Gaby, by Diego Crisostomo"

if __name__ == '__main__':
    app.run()