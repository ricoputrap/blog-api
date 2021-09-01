from api.models.user import UserModel

class UserService:

  def get_all_users(self):
    users = UserModel.query.all()
    return users
  
  def get_user_by_id(self, u_id):
    user = UserModel.query.filter_by(u_id=u_id).first()
    return user