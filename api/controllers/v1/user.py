from flask import make_response, jsonify
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
      else:
        user = self.user_service.get_user_by_id(u_id)

        if not user:
          return make_response(jsonify({
            'errors': {
              'status': 404,
              'title': 'User not found',
              'detail': 'User with u_id = %s is not found' % (u_id),
              'source': {
                'pointer': '/profile/<u_id>',
                'method': 'GET'
              },
            }
          }), 404)
        
        response = {
          'data': self.user_schema.dump(user)
        }
      return response
    except Exception as e:
      return make_response(jsonify({
        'errors': [
          {
            "status": 500,
            "source": { "pointer": "/profile/", "method": "GET" },
            "title": "Internal Server Error",
            "detail": str(e)
          }
        ]
      }), 500)