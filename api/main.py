import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from api.utils import db, migrate

# for initial migration only
from api.models.user import UserModel
from api.models.post import PostModel

def init_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
  
  db.init_app(app)
  migrate.init_app(app, db)

  return app