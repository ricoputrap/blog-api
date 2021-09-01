from werkzeug.security import generate_password_hash
from api.models.user import UserModel
from api.utils import db
import uuid

class UserService:

  def get_all_users(self):
    users = UserModel.query.all()
    return users
  
  def get_user_by_id(self, u_id):
    user = UserModel.query.filter_by(u_id=u_id).first()
    return user

  def create_new_user(self, new_user_data):
    hashed_password = generate_password_hash(new_user_data['u_password'], method='sha256')
    u_id = str(uuid.uuid4())
    
    u_occupation = ""
    if "u_occupation" in new_user_data:
      u_occupation = new_user_data['u_occupation']

    new_user = UserModel(
      u_id = u_id,
      u_username = new_user_data['u_username'],
      u_password = hashed_password,
      u_email = new_user_data['u_email'],
      u_fullname = new_user_data['u_fullname'],
      u_occupation = u_occupation
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user
  
  def edit_user(self, u_id, request_body):
    user = UserModel.query.filter_by(u_id=u_id).first()
    if not user:
      return None
    
    if 'u_email' in request_body:
      user.u_email = request_body['u_email']
    if 'u_fullname' in request_body:
      user.u_fullname = request_body['u_fullname']
    if 'u_occupation' in request_body:
      user.u_occupation = request_body['u_occupation']
    
    db.session.commit()
    return user