from flask import render_template, request, redirect
from flask import Blueprint

from classes.member import Member

import connectors.conn_member as connector_member
import connectors.conn_plan as connector_plan


members_blueprint = Blueprint("members", __name__)


@members_blueprint.route("/members")
def members_index():
    members = connector_member.get_all_active()
    return render_template("members/index.html", members=members, title="Members")
