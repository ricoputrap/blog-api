from flask_restful import Resource
from api.services.user import UserService
from api.serializers.user import UserSchema

class User(Resource):

  user_service = UserService()
  user_schema = UserSchema()
  user_list_schema = UserSchema(many=True)

  def get(self, u_id = None):
    try:
      if u_id == None:
        users = self.user_service.get_all_users()
        response = {
          'data': self.user_list_schema.dump(users),
          'total': len(users)
        }
        return response
      else:
        pass
    except Exception as e:
      pass