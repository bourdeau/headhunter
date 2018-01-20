import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'CHANGE_ME!'
DB_NAME = 'headhunter'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
CSRF_SESSION_KEY = "CHANGE_ME!"
SECRET_KEY = "CHANGE_ME!"
FIXTURES_DIRS = BASE_DIR + '/fixtures'
LOG_DIR = './logs'

# Security (flask_security: http://pythonhosted.org/Flask-Security/configuration.html)
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'CHANGE_ME!'
SECURITY_REGISTERABLE = False
SECURITY_REGISTER_URL = '/register'
SECURITY_LOGIN_URL = '/login'
SECURITY_RESET_URL = '/reset'

# Github
GITHUB_EMAIL = 'CHANGE_ME!'
GITHUB_PASSWORD = 'CHANGE_ME!'
