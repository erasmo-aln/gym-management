from flask import render_template, request, redirect
from flask import Blueprint

from classes.member import Member

import connectors.conn_member as connector_member
import connectors.conn_plan as connector_plan


members_blueprint = Blueprint("members", __name__)


# Route to index page with active members
@members_blueprint.route("/members")
def members_index():
    members = connector_member.get_all_active()
    return render_template("members/index.html", members=members, title="Members")


# Route to show details
@members_blueprint.route("/members/<id_>")
def show_details(id_):
    member = connector_member.get_one(id_)
    activities = connector_member.get_activities(id_)
    plan_type = connector_plan.get_one(member.plan_type.id_)
    return render_template("members/details.html", member=member, plan_type=plan_type, activities=activities, title="Show Details")


