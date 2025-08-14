from flask import render_template, redirect
import config
from models import Person

# Connexion App (integrando OpenAPI via swagger.yaml)
app = config.connex_app
app.add_api(config.basedir / "swagger.yaml")

# Rota principal para renderizar lista de pessoas
# @app.route("/")
# def home():
#     people = Person.query.all()
#     return render_template("home.html", people=people)

# Flask interno para o WSGI
flask_app = app.app

# direcionado para UI da api
@app.route('/')
def redirect_to_swagger():
    return redirect('/api/ui')

# Execução local (útil só para testes; ignorado em produção com Gunicorn)
if __name__ == "__main__":
    app.run()
