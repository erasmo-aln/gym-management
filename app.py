from flask import Flask, render_template

from controllers.controller_member import members_blueprint
from controllers.controller_actitivities import activities_blueprint
from controllers.controller_instructor import instructors_blueprint
from controllers.controller_schedule import schedule_blueprint


app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(activities_blueprint)
app.register_blueprint(instructors_blueprint)
app.register_blueprint(schedule_blueprint)


@app.route("/")
def home():
    return render_template("index.html", title='Home')


if __name__ == "__main__":
    app.run(debug=True)
