from flask import render_template
import config
from models import Person

app = config.connex_app #usando o connexion do config.py
app.add_api(config.basedir / "swagger.yaml")

@app.route("/")
def home():
    people = Person.query.all()
    return render_template("home.html", people=people)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)