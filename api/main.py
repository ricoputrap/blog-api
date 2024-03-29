from api.middleware import AuthMiddleware
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_restful import Api
from api.utils import db, ma, migrate
from api.controllers.v1.user import User
from api.controllers.v1.post import Post


def init_app():
  app = Flask(__name__)
  api = Api(app)

  DB_URI = os.getenv('DATABASE_URL')
  if DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)

  app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
  app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
  
  db.init_app(app)
  ma.init_app(app)
  migrate.init_app(app, db)

  api.add_resource(User, "/profile/", "/profile/<u_id>")
  app.add_url_rule("/register/", endpoint="user", methods=["POST"])
  app.add_url_rule("/login/", endpoint="user", methods=["POST"])
  api.add_resource(Post, "/posts/", "/posts/<p_id>")

  app.wsgi_app = AuthMiddleware(app.wsgi_app)

  return app