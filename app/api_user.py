from app import app
from models import User
from flask import jsonify
from flask import request
from app import db


@app.route('/api/user', methods=['GET'])
def api_user_get():
    users = User.query.all()
    users_json = [{"id": user.id, "name": user.name, "surname": user.surname} for user in users]
    return jsonify(users_json)


@app.route('/api/user/<id>', methods=['GET'])
def api_user_get_id(id):
    users = User.query.filter_by(id=id)
    if not users:
        abort(404)
    user = users[0]
    user_json = {"id": user.id, "name": user.name, "surname": user.surname}
    return jsonify(user_json)


@app.route('/api/user', methods=['POST'])
def api_user_insert():
    new_user = request.get_json()
    user = User(id=new_user['id'], name=new_user['name'], surname=new_user['surname'])
    db.session.add(user)
    db.session.commit()
    user_json = {"id": user.id, "name": user.name, "surname": user.surname}
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
