from flask import render_template, request, redirect
from flask import Blueprint

from classes.activity import Activity

import connectors.conn_activity as connector_activity
import connectors.conn_instructor as connector_instructor
import connectors.conn_plan as connector_plan


activities_blueprint = Blueprint("activities", __name__)


# Route to index page with active activities
@activities_blueprint.route("/activities")
def activities_index():
    activities = connector_activity.get_all_active()
    return render_template("activities/index.html", activities=activities, title="activities")


# Route to an specific activity
@activities_blueprint.route("/activities/<id_>")
def show_details(id_):
    activity = connector_activity.get_one(id_)
    plan_type = connector_plan.get_one(activity.plan_type.id_)
    members = connector_activity.get_members(id_)
    members_booked = len(members)
    instructor = connector_instructor.get_one(activity.instructor)
    return render_template("/activities/details.html", activity=activity, instructor=instructor, members=members, members_booked=members_booked, plan_type=plan_type, title="Activity Details")
