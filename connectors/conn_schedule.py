from classes.scheduler import Scheduler

from database.run_sql import run_sql


def get_all():

    schedule_list = list()

    sql = 'SELECT * FROM webuser.TB_SCHEDULE;'
    result_list = run_sql(sql=sql, values=None)

    for row in result_list:
        schedule = Scheduler(
            activity=row['activity'],
            member=row['member'],
            id_=row['id'])

        schedule_list.append(schedule)

    return schedule_list


def get_one(id_):

    sql = 'SELECT * FROM webuser.TB_SCHEDULE WHERE id = %s;'
    value = [id_]

    result = run_sql(sql=sql, values=value)[0]

    if result is not None:
        schedule = Scheduler(
            activity=result['activity'],
            member=result['member'],
            id_=result['id'])

        return schedule

    return None


def schedule_exists(activity, member):

    sql = 'SELECT * FROM webuser.TB_SCHEDULE WHERE activity = %s AND member = %s;'
    values = [activity, member]

    result_list = run_sql(sql=sql, values=values)

    if len(result_list) == 0:
        return False

    return True


def new(scheduler):

    sql = "INSERT INTO webuser.TB_SCHEDULE (activity, member) VALUES (%s, %s) RETURNING *;"
    values = [scheduler.activity.id_, scheduler.member.id_]

    result = run_sql(sql=sql, values=values)

    scheduler.id_ = result[0]['id']

    return scheduler


def delete_by_id(id_):

    sql = 'DELETE FROM webuser.TB_SCHEDULE WHERE id = %s;'
    value = [id_]

    run_sql(sql=sql, values=value)


def delete_schedule(member, activity):

    sql = 'DELETE FROM webuser.TB_SCHEDULE WHERE activity = %s AND member = %s;'
    values = [activity, member]

    run_sql(sql=sql, values=values)
