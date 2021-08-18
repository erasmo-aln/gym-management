import connectors.conn_plan as plan

from classes.activity import Activity
from classes.member import Member

from database.run_sql import run_sql


# Get all activities, active or not
def get_all():

    activity_list = list()

    sql = 'SELECT * FROM webuser.TB_ACTIVITY;'
    result_list = run_sql(sql=sql, values=None)

    for row in result_list:
        plan_type = plan.get_one(row['plan_type'])

        activity = Activity(
            name=row['name'],
            instructor=row['instructor'],
            date=row['date'],
            duration=row['duration'],
            capacity=row['capacity'],
            plan_type=plan_type,
            active=row['active'],
            id_=row['id'])

        activity_list.append(activity)

    return activity_list


# Get all members given an activity
def get_members(id_):

    member_list = list()

    sql = (
        'SELECT webuser.TB_MEMBER.* '
        'FROM webuser.TB_MEMBER INNER JOIN webuser.TB_SCHEDULE ON webuser.TB_SCHEDULE.member = webuser.TB_MEMBER.id '
        'WHERE webuser.TB_SCHEDULE.activity = %s;')
    value = [id_]

    result_list = run_sql(sql=sql, values=value)

    for row in result_list:
        member = Member(
            name=row['name'],
            lastname=row['lastname'],
            birth_date=row['birth_date'],
            address=row['address'],
            phone=row['phone'],
            email=row['email'],
            plan_type=row['plan_type'],
            begin_date=row['begin_date'],
            active=row['active'],
            id_=row['id'])

        member_list.append(member)

    return member_list


# Get all active activities only
def get_all_active():

    activity_list = list()

    sql = 'SELECT * FROM webuser.TB_ACTIVITY WHERE active = true ORDER BY date ASC;'

    result_list = run_sql(sql=sql, values=None)

    for row in result_list:
        plan_type = plan.get_one(row['plan_type'])

        activity = Activity(
            name=row['name'],
            instructor=row['instructor'],
            date=row['date'],
            duration=row['duration'],
            capacity=row['capacity'],
            plan_type=plan_type,
            active=row['active'],
            id_=row['id'])

        activity_list.append(activity)

    return activity_list


# Get all inactive activities only
def get_all_inactive():

    activity_list = list()

    sql = 'SELECT * FROM webuser.TB_ACTIVITY WHERE active = false ORDER BY date ASC;'

    result_list = run_sql(sql=sql, values=None)

    for row in result_list:
        plan_type = plan.get_one(row['plan_type'])

        activity = Activity(
            name=row['name'],
            instructor=row['instructor'],
            date=row['date'],
            duration=row['duration'],
            capacity=row['capacity'],
            plan_type=plan_type,
            active=row['active'],
            id_=row['id'])

        activity_list.append(activity)

    return activity_list


# Get an activity given its id
def get_one(id_):

    sql = 'SELECT * FROM webuser.TB_ACTIVITY WHERE id = %s;'
    value = [id_]

    result = run_sql(sql=sql, values=value)[0]

    if result is not None:

        plan_type = plan.get_one(result['plan_type'])

        activity = Activity(
            name=result['name'],
            instructor=result['instructor'],
            date=result['date'],
            duration=result['duration'],
            capacity=result['capacity'],
            plan_type=plan_type,
            active=result['active'],
            id_=result['id'])

        return activity

    return None


# Create a new activity
def new(activity):
    sql = 'INSERT INTO webuser.TB_ACTIVITY (name, instructor, date, duration, capacity, plan_type, active) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *;'
    values = [activity.name, activity.instructor, activity.date, activity.duration, activity.capacity, activity.plan_type, activity.active]

    result = run_sql(sql=sql, values=values)[0]

    activity.id_ = result['id']

    return activity


# Delete an activity given its id
def delete_one(id_):
    sql = 'DELETE FROM webuser.TB_ACTIVITY WHERE id = %s'
    value = [id_]

    run_sql(sql=sql, values=value)


# Edit an existing activity
def edit(activity):
    sql = 'UPDATE webuser.TB_ACTIVITY SET (name, instructor, date, duration, capacity, plan_type, active) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s;'
    values = [activity.name, activity.instructor, activity.date, activity.duration, activity.capacity, activity.plan_type, activity.active, activity.id_]

    run_sql(sql=sql, values=values)
