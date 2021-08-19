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


# Route to edit member's data
@members_blueprint.route("/members/<id_>/edit")
def edit_member(id_):
    member = connector_member.get_one(id_)
    plans = connector_plan.get_all()
    return render_template("/members/edit.html", member=member, plans=plans, title="Edit Member's Details")


# Route to the POST edit
@members_blueprint.route("/members/<id_>", methods=["POST"])
def update_member(id_):
    name = request.form["name"]
    lastname = request.form['lastname']
    birth_date = request.form['birth_date']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    plan_type = request.form['plan_type']
    begin_date = request.form['begin_date']
    active = request.form['active']
    plan = connector_plan.get_one(plan_type)

    updated_member = Member(name, lastname, birth_date, address, phone, email, plan.id_, begin_date, active, id_)
    connector_member.edit(updated_member)
    return redirect("/members")
