from api.utils import db

class UserModel(db.Model):
  __tablename__ = 'User'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.String(50), nullable=False, unique=True)
  username = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(255), nullable=False, unique=True)
  fullname = db.Column(db.String(255), nullable=False)
  occupation = db.Column(db.String(255), nullable=True)