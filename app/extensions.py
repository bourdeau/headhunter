from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
security = Security()
ma = Marshmallow()
cors = CORS()
