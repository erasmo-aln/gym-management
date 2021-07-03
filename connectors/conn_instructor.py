from classes.instructor import Instructor
from classes.activity import Activity

from database.run_sql import run_sql


def get_all():

    instructor_list = list()

    sql = 'SELECT * FROM webuser.TB_INSTRUCTOR;'
    results = run_sql(sql, values=None)

    for row in results:
        instructor = Instructor(
            name=row['name'],
            lastname=row['lastname'],
            birth_date=row['birth_date'],
            address=row['address'],
            phone=row['phone'],
            id_=row['id_'])

        instructor_list.append(instructor)

    return instructor_list


def get_one(id_):

    sql = 'SELECT * FROM webuser.TB_INSTRUCTOR WHERE id = %s;'
    value = [id_]

    result = run_sql(sql, value)[0]

    if result is not None:
        instructor = Instructor(
            name=result['name'],
            lastname=result['lastname'],
            birth_date=result['birth_date'],
            address=result['address'],
            phone=result['phone'],
            id_=result['id_'])

    return instructor


def get_activities(id_):

    activity_list = list()

    sql = 'SELECT * FROM webuser.TB_ACTIVITY WHERE instructor = %s;'
    value = [id_]

    results = run_sql(sql, value)

    for row in results:
        activity = Activity(
            name=row['name'],
            instructor=row['instructor'],
            date=row['date'],
            duration=row['duration'],
            capacity=row['capacity'],
            plan_type=row['plan_type'],
            active=row['active'],
            id_=row['id_'])

        activity_list.append(activity)

    return activity_list


def new(instructor):

    sql = 'INSERT INTO webuser.TB_INSTRUCTOR (name, lastname, birth_date, address, phone) VALUES (%s, %s, %s, %s, %s) RETURNING *;'
    values = [instructor.name, instructor.lastname, instructor.birth_date, instructor.address, instructor.phone]

    result = run_sql(sql, values)[0]

    instructor.id_ = result['id_']

    return instructor


def delete_one(id_):

    sql = 'DELETE FROM webuser.TB_INSTRUCTOR WHERE id = %s;'
    value = [id_]
    run_sql(sql, value)


def edit(instructor):

    sql = 'UPDATE webuser.TB_INSTRUCTOR SET (name, lastname, birht_date, address, phone) = (%s, %s, %s, %s, %s) WHERE id = %s;'
    values = [instructor.name, instructor.lastname, instructor.birth_date, instructor.address, instructor.phone, instructor.id_]
    run_sql(sql, values)
