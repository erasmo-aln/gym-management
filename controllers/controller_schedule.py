from flask import render_template, request, redirect
from flask import Blueprint

from classes.scheduler import Scheduler

import connectors.conn_schedule as connector_schedule
import connectors.conn_member as connector_member
import connectors.conn_activity as connector_activity
import connectors.conn_plan as connector_plan


schedule_blueprint = Blueprint("schedules", __name__)


@schedule_blueprint.route("/schedule/new/member/<id_>")
def new_member_schedule(id_):
    member = connector_member.get_one(id_)
    activities = connector_activity.get_all_active()
    return render_template("schedule/new-member.html", member=member, activities=activities, title="New Schedule")


@schedule_blueprint.route("/schedule/member", methods=['POST'])
def create_schedule_from_member():
    activity_id = request.form['activity']
    member_id = request.form['member']

    activity = connector_activity.get_one(activity_id)
    member = connector_member.get_one(member_id)
    member_plan = connector_plan.get_one(member.plan_type.id_)
    activity_plan = connector_plan.get_one(activity.plan_type.id_)
    current_schedules = len(connector_activity.get_members(activity_id))
    activities = connector_activity.get_all_active()

    if connector_schedule.schedule_exists(activity_id, member_id):
        error = "Schedule already created."
        return render_template("schedule/new-member.html", member=member, activities=activities, error=error, title="New Schedule")

    elif member_plan.plan == "Monthly" and activity_plan.plan == "Annually":
        error = "Your plan must be Annually."
        return render_template("schedule/new-member.html", member=member, activities=activities, error=error, title="New Schedule")

    elif current_schedules >= activity.capacity:
        error = "This activity is at full capacity."
        return render_template("schedule/new-member.html", member=member, activities=activities, error=error, title="New Schedule")

    else:
        new_schedule = Scheduler(activity, member)
        connector_schedule.new(new_schedule)
        member_page = "/members/" + member_id
        return redirect(member_page)


# Route to delete an scheduled activity from an specific member
@schedule_blueprint.route("/schedule/delete/members/<member_id>/<activity_id>")
def delete_scheduled_activity(member_id, activity_id):
    connector_schedule.delete_schedule(member_id, activity_id)
    schedule_page = "/members/" + member_id
    return redirect(schedule_page)
