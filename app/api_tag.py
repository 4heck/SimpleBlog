from app import app
from models import Tag
from flask import jsonify
from flask import request
from app import db


@app.route('/api/tag', methods=['GET'])
def api_tag_get():
    tags = Tag.query.all()
    tags_json = [{"id": tag.id, "name": tag.name, "slug": tag.slug} for tag in tags]
    return jsonify(tags_json)


@app.route('/api/tag/<id>', methods=['GET'])
def api_tag_get_id(id):
    tags = Tag.query.filter_by(id=id)
    if not tags:
        abort(404)
    tag = tags[0]
    tag_json = {"id": tag.id, "name": tag.name, "slug": tag.slug}
    return jsonify(tag_json)


@app.route('/api/tag', methods=['POST'])
def api_tag_insert():
    new_tag = request.get_json()
    tag = Tag(name=new_tag['name'])
    db.session.add(tag)
    db.session.commit()
    tag_json = {"id": tag.id, "name": tag.name, "slug": tag.slug}
    return jsonify(tag_json)


@app.route('/api/tag/<id>', methods=['DELETE'])
def api_tag_delete(id):
    tags = Tag.query.filter_by(id=id)
    if not tags:
        abort(404)
    tag = tags[0]
    db.session.delete(tag)
    db.session.commit()
    return jsonify()
