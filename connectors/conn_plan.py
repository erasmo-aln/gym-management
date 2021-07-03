from classes.plan import PlanType

from database.run_sql import run_sql


def get_all():
    plan_type_list = list()

    sql = 'SELECT * FROM WEBUSER.TB_PLAN'
    results = run_sql(sql=sql, values=None)

    for row in results:
        plan_type = PlanType(row['plan'], row['id_'])
        plan_type_list.append(plan_type)

    return plan_type_list


def get_one(id_):
    sql = 'SELECT * FROM WEBUSER.TB_PLAN WHERE id = %s'
    value = [id_]

    result = run_sql(sql, value)[0]

    if result is not None:
        plan_type = PlanType(result['plan'], result['id_'])

    return plan_type


def new(plan_type):
    sql = 'INSERT INTO WEBUSER.TB_PLAN (plan) VALUES (%s) RETURNING *;'
    values = [plan_type.plan]

    result = run_sql(sql, values)[0]

    plan_type.id_ = result['id_']

    return plan_type


def delete_one(id_):
    sql = 'DELETE FROM WEBUSER.TB_PLAN WHERE id = %s;'
    value = [id_]

    run_sql(sql, value)


def edit(plan_type):
    sql = 'UPDATE WEBUSER.TB_PLAN SET (plan) = (%s) WHERE id = %s;'
    values = [plan_type.plan, plan_type.id_]

    run_sql(sql, values)
