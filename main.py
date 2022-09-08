import json
from flask import request
from Config import app
from models import User, Order, Offer
from service import init_db, get_all, get_by_id, insert_data_user


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user([request.json])
        else:
            print('Не известный тп данных')

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>", methods=['GET', 'PUT'])
def get_by_id_users(user_id):
    if request.method == 'GET':
        data = get_by_id(User, user_id)
        return app.response_class(
            response=json.dumps(data, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        pass


@app.get("/orders/")
def get_orders():
    return app.response_class(
        response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.get("/orders/<int:order_id>")
def get_by_id_orders(order_id):
    data = get_by_id(Order, order_id)

    return app.response_class(
        response=json.dumps(data, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.get("/offers/")
def get_offers():
    return app.response_class(
        response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.get("/offers/<int:offer_id>")
def get_by_id_offers(offer_id):
    data = get_by_id(Offer, offer_id)

    return app.response_class(
        response=json.dumps(data, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
