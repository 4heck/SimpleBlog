from flask import Blueprint
from flask import render_template
from models import Post, Tag
from flask import request
from .forms import PostForm
from app import db
from flask import redirect
from flask import url_for

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/create', methods=['POST','GET'])
def create_post():
	if request.method=='POST':
		title=request.form['title']
		body=request.form['body']

		try:
			post = Post(title=title, body=body)
			db.session.add(post)
			db.session.commit()
		except:
			print('Something wrong')
		return redirect(url_for('posts.index'))

	form = PostForm()
	tags =Tag.query.all()
	return render_template('posts/create_post.html', form=form, tags=tags)

@posts.route('/')
def index():
	q=request.args.get('q')
	result="null"
	if q:
		result=q
		if Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all():
			posts=Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
		else:
			posts="0"
	else:
		posts = Post.query.order_by(Post.created.desc())
	tags =Tag.query.all()
	return render_template('posts/index.html', posts=posts, tags=tags, result=result)

@posts.route('/<slug>')
def post_detail(slug):
	post = Post.query.filter(Post.slug==slug).first()
	tags = post.tags
	#date = datetime.fromtimestamp(post.created)
	return render_template('posts/post_detail.html', post=post, tags=tags)

@posts.route('/tag/<slug>')
def tag_detail(slug):
	tag = Tag.query.filter(Tag.slug==slug).first()
	posts = tag.posts.all()
	return render_template('posts/tag_detail.html', tag=tag, posts=posts)


