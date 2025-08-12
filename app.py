from flask import render_template
import config
from models import Person

# Connexion App (integrando OpenAPI via swagger.yaml)
app = config.connex_app
app.add_api(config.basedir / "swagger.yaml")

# Rota principal para renderizar lista de pessoas
@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

# Execução local (útil só para testes; ignorado em produção com Gunicorn)
if __name__ == "__main__":
    app.run()
