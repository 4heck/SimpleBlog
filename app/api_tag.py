from app import app
from models import Tag
from flask import jsonify
from flask import render_template
from flask import request
import json
from app import db


@app.route('/api/tag', methods=['GET'])
def api_tag_get():
    tags = Tag.query.all()
    tags_json = [{"id": tag.id, "name": tag.name, "slug": tag.slug} for tag in tags]
    return jsonify(tags_json)


@app.route('/api/tag/<id>', methods=['GET'])
def api_tag_get_id(id):
    tags = Tag.query.filter_by(id=id)
    try:
        tag = tags[0]
        tag_json = {"id": tag.id, "name": tag.name, "slug": tag.slug}
        return jsonify(tag_json)
    except:
        return render_template('404.html')


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
    try:
        tag = tags[0]
        db.session.delete(tag)
        db.session.commit()
        return jsonify()
    except:
        return render_template('404.html')


@app.route('/api/tag/<id>', methods=['PUT'])
def api_tag_update(id):
    updated_tag = request.get_json()
    tags_to_update = Tag.query.filter_by(id=id)
    try:
        data = json.loads(request.get_data())
        tag_to_update = tags_to_update[0]
        tag_to_update = db.session.query(Tag).filter_by(id = id).first()
        tag_to_update.name = data['name']
        tag_to_update.slug = data['slug']
        db.session.commit()
        return jsonify(tag_to_update.to_dict())
    except:
        return render_template('404.html')