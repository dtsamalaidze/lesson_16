import json

from models import *
from Config import db


def insert_data_user(input_data):
    for row in input_data:
        db.session.add(
            User(
                id=row.get('id'),
                first_name=row.get('first_name'),
                last_name=row.get('last_name'),
                age=row.get('age'),
                email=row.get('email'),
                role=row.get('role'),
                phone=row.get('phone'),
            )
        )
    db.session.commit()


def insert_data_order(input_data):
    for row in input_data:
        db.session.add(
            Order(
                id=row.get('id'),
                name=row.get('name'),
                description=row.get('description'),
                start_date=row.get('start_date'),
                end_date=row.get('end_date'),
                address=row.get('address'),
                price=row.get('price'),
                customer_id=row.get('customer_id'),
                executor_id=row.get('executor_id')
            )
        )
    db.session.commit()


def insert_data_offers(input_data):
    for row in input_data:
        db.session.add(
            Offer(
                id=row.get('id'),
                order_id=row.get('order_id'),
                executor_id=row.get('executor_id'),
            )
        )

    db.session.commit()


def get_all(model):
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())
    return result


def get_by_id(model, _id):
    try:
        return db.session.query(model).get(_id).to_dict()
    except Exception:
        return {}

def update_universal(model, _id, values):
    try:
        db.session.query(model).filter(model.id == _id).update(values)
        db.session.commit()
    except Exception:
        return {}


def init_db():
    db.drop_all()
    db.create_all()
    with open('data/User.json') as file:
        insert_data_user(json.load(file))
    with open('data/Orders.json') as file:
        insert_data_order(json.load(file))
    with open('data/Offers.json') as file:
        insert_data_offers(json.load(file))
