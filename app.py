from flask import Flask, render_template

from controllers.controller_member import members_blueprint
from controllers.controller_actitivities import activities_blueprint


app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)

@app.route("/")
def home():
    return render_template("index.html", title='Home')


if __name__ == "__main__":
    app.run(debug=True)
