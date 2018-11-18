class Configuration(object):
	DEBUG = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	#SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://forblog:1@localhost/test1'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://UserOne:1@localhost/test1'