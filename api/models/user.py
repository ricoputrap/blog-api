from api.utils import db

class UserModel(db.Model):
  __tablename__ = 'tb_user'
  u_id = db.Column(db.String(50), primary_key=True)
  u_username = db.Column(db.String(50), nullable=False, unique=True)
  u_password = db.Column(db.String(255), nullable=False)
  u_email = db.Column(db.String(255), nullable=False, unique=True)
  u_fullname = db.Column(db.String(255), nullable=False)
  u_occupation = db.Column(db.String(255), nullable=True)