import connectors.conn_plan as plan

from classes.activity import Activity
from classes.member import Member

from database.run_sql import run_sql


# Get all members, regardless if they're active or not
def get_all():

    member_list = list()

    sql = 'SELECT * FROM webuser.TB_MEMBER ORDER BY name ASC;'
    result_list = run_sql(sql=sql, values=None)

    for row in result_list:
        plan_type = plan.get_one(row['plan_type'])

        member = Member(
            name=row['name'],
            lastname=row['lastname'],
            birth_date=row['birth_date'],
            address=row['address'],
            phone=row['phone'],
            email=row['email'],
            plan_type=plan_type,
            begin_date=row['begin_date'],
            active=row['active'],
            id_=row['id'])

        member_list.append(member)

    return member_list


# Get a specific member
def get_one(id_):

    sql = 'SELECT * FROM webuser.TB_MEMBER WHERE id = %s;'
    value = [id_]

    result = run_sql(sql=sql, values=value)[0]

    if result is not None:
        plan_type = plan.get_one(result['plan_type'])

        member = Member(
            name=result['name'],
            lastname=result['lastname'],
            birth_date=result['birth_date'],
            address=result['address'],
            phone=result['phone'],
            email=result['email'],
            plan_type=plan_type,
            begin_date=result['begin_date'],
            active=result['active'],
            id_=result['id'])

        return member

    return None


# Get all activities given the member id
def get_activities(id_):

    activity_list = list()

    sql = (
        'SELECT * '
        'FROM webuser.TB_ACTIVITY '
        'INNER JOIN webuser.TB_SCHEDULE ON webuser.TB_SCHEDULE.activity = webuser.TB_ACTIVITY.id '
        'WHERE webuser.TB_SCHEDULE.member = %s;')
    value = [id_]

    result_list = run_sql(sql=sql, values=value)

    for row in result_list:
        plan_type = plan.get_one(id_=row['plan_type'])

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


# Get all active members
def get_all_active():

    member_list = list()

    sql = 'SELECT * FROM webuser.TB_MEMBER WHERE active = true ORDER BY name ASC;'

    result_list = run_sql(sql=sql, values=None)

    for row in result_list:
        plan_type = plan.get_one(id_=row['plan_type'])

        member = Member(
            name=row['name'],
            lastname=row['lastname'],
            birth_date=row['birth_date'],
            address=row['address'],
            phone=row['phone'],
            email=row['email'],
            plan_type=plan_type,
            begin_date=row['begin_date'],
            active=row['active'],
            id_=row['id'])

        member_list.append(member)

    return member_list


def get_all_inactive():

    member_list = list()

    sql = 'SELECT * FROM webuser.TB_MEMBER WHERE active = false ORDER BY name ASC;'

    result_list = run_sql(sql=sql, values=None)

    for row in result_list:
        plan_type = plan.get_one(id_=row['plan_type'])

        member = Member(
            name=row['name'],
            lastname=row['lastname'],
            birth_date=row['birth_date'],
            address=row['address'],
            phone=row['phone'],
            email=row['email'],
            plan_type=plan_type,
            begin_date=row['begin_date'],
            active=row['active'],
            id_=row['id'])

        member_list.append(member)
    return


# Create new member
def new(member):

    sql = 'INSERT INTO webuser.TB_MEMBER (name, lastname, birth_date, address, phone, email, plan_type, begin_date, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;'
    values = [member.name, member.lastname, member.birth_date, member.address, member.phone, member.email, member.plan_type, member.begin_date, member.active]

    result = run_sql(sql=sql, values=values)[0]

    member.id_ = result['id']

    return member


# Delete a member given its id
def delete_one(id_):

    sql = 'DELETE FROM webuser.TB_MEMBER WHERE id = %s;'
    value = [id_]
    run_sql(sql=sql, values=value)


# Edit a member given its id
def edit(member):

    sql = 'UPDATE webuser.TB_MEMBER SET (name, lastname, birth_date, address, phone, email, plan_type, begin_date, active) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s;'
    values = [member.name, member.lastname, member.birth_date, member.address, member.phone, member.email, member.plan_type, member.begin_date, member.active, member.id_]

    run_sql(sql=sql, values=values)
