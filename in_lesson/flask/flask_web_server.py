import random

from flask import Flask, request, jsonify
import psycopg2
import json

app = Flask("bank_web_app")

# need to change to your database
conn: psycopg2._psycopg.connection = psycopg2.connect(host="localhost",
                        port=5432,
                        database='bank_db',
                        user="postgres",
                        password='Avia@1601')

@app.route("/api/v1/customers", methods=['GET'])
def get_customer():
    """
    The function get query params and returns or the all customers or with filter
    params: page_num, results_per_page, passport_num, name_customer, address
    """

    page_num = request.args.get('page_num')
    results_per_page = request.args.get('results_per_page')
    # passport_num = int(request.args.get('passport_num')) if request.args.get('passport_num') is not None else None
    # name_customer = request.args.get('name_contains')
    # address = request.args.get('address')
    default_num_page = 20
    js = {}

    query_param = []
    query_value = []
    for arg in request.args:
        if request.args.get(arg) is not None and arg != 'page_num' and arg != 'results_per_page':
            if arg == 'passport_num':
                query_value.append(f"{arg}")
                query_value.append(int(request.args[arg]))

                query_param.append("%s = %i")
            else:
                query_value.append(f"{arg}")
                query_value.append(f"'%{request.args[arg]}%'")

                query_param.append(f"%s ilike %s")

    # print(query_param, query_value)

    with conn:
        with conn.cursor() as cur:

            if len(query_param) == 0:
                sql = "SELECT * FROM customer"
                cur.execute(sql)
            else:
                sql = f"SELECT * FROM customer WHERE {'and'.join(query_param)}" % (tuple(query_value))
                # sql = "SELECT * FROM customer WHERE " + 'and'.join(query_param) % (tuple(query_value))
                cur.execute(sql)

            # TODO: ask valeria need to add num page

            results = cur.fetchmany(int(results_per_page) if results_per_page is not None else default_num_page)
            if results:
                for result in results:
                    js[result[0]] = {
                        'id': result[0],
                        'passport_num': result[1],
                        'name': result[2],
                        'address': result[3]
                    }
                return jsonify(js)
            else:
                return app.response_class(status=404)


@app.route("/api/v1/customers", methods=['POST'])
def create_customer():
    """
    The function create new customer
    params: passport_num -> int, name_customer -> str with '': 'Ronit', address -> str with '': 'Tel Aviv'
    """
    new_data = request.form
    placeholders = tuple(new_data.keys()) + tuple(new_data.values())
    sql = "INSERT INTO customer (%s, %s, %s) VALUES(%s, %s, %s);" % (tuple(placeholders))

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(new_data.keys()) + tuple(new_data.values()))
            if cur.rowcount == 1:
                return app.response_class(status=200)
    return app.response_class(status=200)


@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def get_customer_by_id(customer_id):
    print(f"called /customers/customer_id/{customer_id}")
    with conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM customer WHERE id = %s"
            cur.execute(sql, (customer_id,))
            result = cur.fetchone()
            if result:
                ret_data = {
                    'id': result[0],
                    'passport_num': result[1],
                    'name': result[2],
                    'address': result[3]
                }
                # option I
                # response = app.response_class(
                #     response=json.dumps(ret_data),
                #     status=200,
                #     mimetype='application/json'
                # )
                # return response

                # option II
                return jsonify(ret_data)
            else:
                return app.response_class(
                    status=404
                )


@app.route("/api/v1/customers/<int:customer_id>", methods=['PUT'])
def update_customer(customer_id):
    """
    the function get the id customer that want to update and query params of what the user want to change
    """
    new_fields = request.form
    query_list = []
    for field in new_fields:
        query_list.append(f"{field}=%s")
    sql = f"UPDATE customer SET {','.join(query_list)} WHERE id=%s"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(new_fields.values()) + tuple([customer_id]))
            if cur.rowcount == 1:
                return app.response_class(status=200)
    return app.response_class(status=500)



@app.route("/api/v1/customers/<int:customer_id>", methods=['DELETE'])
def delete_costumer():
    pass


@app.route("/api/v1/customers/<int:customer_id>/account", methods=['GET'])
def get_account_by_customer_id(customer_id):
    """
    The function get customer id and return his accounts
    """
    sql = """
            select c.passport_num ,a.id, a.account_num, a.balance, a.max_limit  
            from account_holders ah 
            join customer c on ah.customer_id = c.id
            join account a on ah.account_id = a.id 
            where c.id = %s;
    """
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, (customer_id,))
            result = cur.fetchone()
            if result:
                ret_data = {
                    'passport_num': result[0],
                    'id': result[1],
                    'account_num': result[2],
                    'balance': result[3],
                    'max_limit': result[4]
                }

                return jsonify(ret_data)
            else:
                return app.response_class(
                    status=404
                )


@app.route("/api/v1/account/<int:account_id>", methods=['GET'])
def get_account_by_id(account_id):
    """
    The function return account details by sql id
    """
    with conn:
        with conn.cursor() as cur:
            sql = "SELECT * FROM account WHERE id = %s"
            cur.execute(sql, (account_id,))
            result = cur.fetchone()
            if result:
                ret_data = {
                    'id': result[0],
                    'account_num': result[1],
                    'max_limit': result[2],
                    'balance': result[3]
                }

                return jsonify(ret_data)
            else:
                return app.response_class(
                    status=404
                )


@app.route("/api/v1/account", methods=['GET'])
def get_accounts():
    """
    The function get query params and returns or the all accounts or with filter
    """
    page_num = request.args.get('page_num')
    results_per_page = request.args.get('results_per_page')
    default_num_page = 20
    js = {}

    query_param = []
    query_value = []
    for arg in request.args:
        if request.args.get(arg) is not None and arg != 'page_num' and arg != 'results_per_page':
            query_value.append(f"{arg}")
            query_value.append(int(request.args[arg]))

            query_param.append("%s = %i")

    # print(query_param, query_value)

    with conn:
        with conn.cursor() as cur:

            if len(query_param) == 0:
                sql = "SELECT * FROM account"
                cur.execute(sql)
            else:
                sql = f"SELECT * FROM account WHERE {'and'.join(query_param)}" % (tuple(query_value))
                cur.execute(sql)

            # TODO: ask valeria need to add num page

            results = cur.fetchmany(int(results_per_page) if results_per_page is not None else default_num_page)
            if results:
                for result in results:
                    js[result[0]] = {
                        'id': result[0],
                        'account_num': result[1],
                        'max_limit': result[2],
                        'balance': result[3]
                    }
                return jsonify(js)
            else:
                return app.response_class(status=404)

@app.route("/api/v1/account", methods=['POST'])
def create_account():
    """
    The function create new customer
    params: customer_id -> int: The customer for whom you want to open an account,
            max_limit -> int, balance -> int
    """
    new_data = request.form
    new_account_num = random.randint(100000, 1000000)
    quary_params = []
    quary_value = []
    for data in new_data:
        if data == 'customer_id':
            quary_params.append('account_num')
            quary_value.append(new_account_num)
        else:
            quary_params.append(data)
            quary_value.append(new_data[data])

    placeholders = tuple(quary_params) + tuple(quary_value)
    sql = "INSERT INTO account (%s, %s, %s) VALUES(%s, %s, %s);" % (tuple(placeholders))
    sql_id_account = f"select id from account where account_num = {new_account_num};"
    sql_in_holders = "INSERT INTO account_holders (account_id, customer_id) VALUES(%s, %s)"

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            if cur.rowcount == 1:
                cur.execute(sql_id_account)
                result = cur.fetchone()
                cur.execute(sql_in_holders, (result[0], new_data['customer_id']))
                if cur.rowcount == 1:
                    return app.response_class(status=200)
    return app.response_class(status=500)


@app.route("/api/v1/account/<int:account_id>/deposit", methods=['POST'])
def deposit():
    """
    The function get from body (amount) and update the account balance
    """
    # get balance
    # balance + amount
    # update balance
    pass


@app.route("/api/v1/account/<int:account_id>/withdraw", methods=['POST'])
def withdraw():
    """
    The function get query param (amount) and update the account balance if it possible
    """
    # get balance and max_limit
    # balance vs amount
    # balance - amount
    # update balance
    pass


@app.route("/api/v1/account/<int:account_id>/transfer", methods=['POST'])
def transfer():
    """
    The function get query param (amount and receiving account) and update the account balance if it possible
    """
    # get customer id from account id
    # check amount vs balance
    # insert to transfer
    # update sender
    # update receiver
    pass


@app.route("/api/v1/account/<int:account_id>", methods=['DELETE'])
def delete_account():
    pass




if __name__ == '__main__':
    app.run(debug=True)








