from app import app
import psycopg2
import view
from app import db
from posts.blueprint import posts
import api_post
import api_user
import api_tag

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
	app.run(debug=True)