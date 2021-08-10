from flask import render_template, request, redirect
from flask import Blueprint

from classes.activity import Activity

import connectors.conn_activity as connector_activity
import connectors.conn_instructor as connector_instructor
import connectors.conn_plan as connector_plan


activities_blueprint = Blueprint("activities", __name__)


@activities_blueprint.route("/activities")
def activities_index():
    activities = connector_activity.get_all_active()
    return render_template("activities/index.html", activities=activities, title="activities")

