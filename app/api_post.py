from app import app
from models import Post
from models import Tag
from flask import jsonify
from flask import request
import json
from app import db


@app.route('/api/post', methods=['GET'])
def api_post_get():
    posts = Post.query.all()
    tags = Tag.query.all()
    posts_json = [{"id": post.id, "title": post.title, "body": post.body, "slug": post.slug, "created": post.created}
                  for post in posts]
    return jsonify(posts_json)


@app.route('/api/post/<id>', methods=['GET'])
def api_post_get_id(id):
    posts = Post.query.filter_by(id=id)
    if not posts:
        abort(404)
    post = posts[0]
    post_json = {"id": post.id, "title": post.title, "body": post.body, "slug": post.slug, "created": post.created}
    return jsonify(post_json)


@app.route('/api/post', methods=['POST'])
def api_post_insert():
    new_post = request.get_json()
    post = Post(title=new_post['title'], body=new_post['body'])
    db.session.add(post)
    db.session.commit()
    post_json = {"id": post.id, "title": post.title, "body": post.body, "slug": post.slug, "created": post.created}
    return jsonify(post_json)


@app.route('/api/post/<id>', methods=['DELETE'])
def api_post_delete(id):
    posts = Post.query.filter_by(id=id)
    if not posts:
        abort(404)
    post = posts[0]
    db.session.delete(post)
    db.session.commit()
    return jsonify()


@app.route('/api/post/<id>', methods=['PUT'])
def api_post_update(id):
    updated_post = request.get_json()
    posts_to_update = Post.query.filter_by(id=id)
    if not posts_to_update:
        abort(404)
    data = json.loads(request.get_data())
    post_to_update = posts_to_update[0]
<<<<<<< HEAD
    post_to_update = db.session.query(Post).filter_by(id = id).first()
    post_to_update.title = data['title']
    post_to_update.body = data['body']
    post_to_update.slug = data['slug']
    post_to_update.created = data['created']
=======
    post_to_update.title = updated_post["title"]
    post_to_update.generate_slug()
    post_to_update.body = updated_post["body"]
    db.session.save(updated_post)
>>>>>>> 13d7380096f16de50d53aa2ea1abd291dc9fbab2
    db.session.commit()
    return jsonify(post_to_update.to_dict())