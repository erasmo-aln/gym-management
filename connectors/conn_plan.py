from classes.plan import PlanType
from database.run_sql import run_sql


def get_all():
    plan_type_list = list()

    sql = 'SELECT * FROM WEBUSER.TB_PLAN'
    results = run_sql(sql=sql, values=None)

    for row in results:
        plan_type = PlanType(row['plan'], row['id'])
        plan_type_list.append(plan_type)

    return plan_type_list


def get_one(id):
    sql = 'SELECT * FROM WEBUSER.TB_PLAN WHERE id = %s'
    value = [id]

    result = run_sql(sql, value)[0]

    if result is not None:
        plan_type = PlanType(result['plan'], result['id'])

    return plan_type


def new(plan_type):
    sql = 'INSERT INTO WEBUSER.TB_PLAN (plan) VALUES (%s) RETURNING *;'
    values = [plan_type.plan]

    result = run_sql(sql, values)

    plan_type.id = result[0]['id']

    return plan_type


def delete_one(id):
    sql = 'DELETE FROM WEBUSER.TB_PLAN WHERE id = %s;'
    value = [id]

    run_sql(sql, value)


def edit(plan_type):
    sql = 'UPDATE WEBUSER.TB_PLAN SET (plan) = (%s) WHERE id = %s;'
    values = [plan_type.plano, plan_type.id]

    run_sql(sql, values)
