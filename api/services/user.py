from api.models.user import UserModel

class UserService:

  def get_all_users(self):
    users = UserModel.query.all()
    return users