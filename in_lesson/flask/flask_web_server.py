from flask import Flask, request, jsonify
import psycopg2
import json

app = Flask("bank_web_app")

# need to change to your database
conn: psycopg2._psycopg.connection = psycopg2.connect(host="localhost",
                        port=5432,
                        database='bank',
                        user="postgres",
                        password='Avia@1601')


@app.route("/api/v1/customers")
def hello_world():
    return "Hello, World!"

@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def get_customer(customer_id):
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


@app.route("/beauty")
def beauty_html():
    return "<h1>Hi</h1>" \
           "<p style= 'color: red'>HELLO YOU</p>"






if __name__ == '__main__':
    app.run(debug=True)








