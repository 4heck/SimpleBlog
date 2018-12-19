from app import app
from models import User
from flask import jsonify
from flask import request
import json
from app import db


@app.route('/api/user', methods=['GET'])
def api_user_get():
    users = User.query.all()
    users_json = [{"id": user.id, "name": user.name, "surname": user.surname, "city": user.city, "email": user.email, "created_account": user.created_account} for user in users]
    return jsonify(users_json)


@app.route('/api/user/<id>', methods=['GET'])
def api_user_get_id(id):
    users = User.query.filter_by(id=id)
    if not users:
        abort(404)
    user = users[0]
    user_json = {"id": user.id, "name": user.name, "surname": user.surname, "city": user.city, "email": user.email, "created_account": user.created_account}
    return jsonify(user_json)


@app.route('/api/user', methods=['POST'])
def api_user_insert():
    new_user = request.get_json()
    user = User(id=new_user['id'], name=new_user['name'], surname=new_user['surname'], city=new_user['city'], email=new_user['email'], created_account=new_user['created_account'])
    db.session.add(user)
    db.session.commit()
    user_json = {"id": user.id, "name": user.name, "surname": user.surname, "city": user.city, "email": user.email, "created_account": user.created_account}
    return jsonify(user_json)


@app.route('/api/user/<id>', methods=['DELETE'])
def api_user_delete(id):
    users = User.query.filter_by(id=id)
    if not users:
        abort(404)
    user = users[0]
    db.session.delete(user)
    db.session.commit()
    return jsonify()

@app.route('/api/user/<id>', methods=['PUT'])
def api_user_update(id):
    updated_user = request.get_json()
    users_to_update = User.query.filter_by(id=id)
    if not users_to_update:
        abort(404)
    data = json.loads(request.get_data())
    user_to_update = users_to_update[0]
    user_to_update = db.session.query(User).filter_by(id = id).first()
    user_to_update.name = data['name']
    user_to_update.surname = data['surname']
    user_to_update.city = data['city']
    user_to_update.email = data['email']
    user_to_update.created_account = data['created_account']
    db.session.commit()
    return jsonify(user_to_update.to_dict())