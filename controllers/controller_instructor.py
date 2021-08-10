from flask import render_template, request, redirect
from flask import Blueprint

from classes.instructor import Instructor
import connectors.conn_instructor as connector_instructor


instructors_blueprint = Blueprint("instructors", __name__)


@instructors_blueprint.route("/instructors")
def instructors_index():
    instructors = connector_instructor.get_all()
    return render_template("instructors/index.html", instructors=instructors, title="instructors")
