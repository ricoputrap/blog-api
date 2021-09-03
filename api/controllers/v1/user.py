from flask import make_response, jsonify, request
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
          'message': "Get all registered users is success!",
          'data': {
            'users': self.user_list_schema.dump(users),
            'total': len(users)
          }
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
          'message': 'Get user by u_id is success!',
          'data': {
            'user': self.user_schema.dump(user),
          }
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
  
  def post(self):
    path = request.path
    try:
      if path == '/register/':
        request_body = request.get_json()
        new_user = self.user_service.create_new_user(request_body)
        response = {
          'data': {
            'user': self.user_schema.dump(new_user),
            # 'token': 'dummytoken1234'
          },
          'message': 'New user is successfully created!'
        }
        return response
      elif path == '/login/':
        request_body = request.get_json()
        result = self.user_service.login(request_body)
        if not result:
          return make_response(jsonify({
            'errors': [
              {
                "status": 401,
                "source": { "pointer": "/login/", "method": "POST" },
                "title": "Unauthorized",
                "detail": "Wrong username or password."
              }
            ]
          }), 401)
        
        response = {
          "message": "Login successful.",
          "data": {
            "user": self.user_schema.dump(result['user']),
            "token": result['token']
          }
        }
        return response
      else:
        return make_response(jsonify({
        'errors': [
          {
            "status": 404,
            "source": { "pointer": "/profile/", "method": "POST" },
            "title": "Internal Server Error",
            "detail": "Accessible only through /register and /login endpoint"
          }
        ]
      }), 404)
    except Exception as e:
      return make_response(jsonify({
        'errors': [
          {
            "status": 500,
            "source": { "pointer": "%s" % (path), "method": "POST" },
            "title": "Internal Server Error",
            "detail": str(e)
          }
        ]
      }), 500)
  
  def put(self, u_id = None):
    '''
    @TODO set error if `request_body` is empty
    '''
    try:
      if not u_id:
        return make_response(jsonify({
            'errors': [
              {
                "status": 400,
                "source": { "pointer": "/profile/<u_id>", "method": "PUT" },
                "title": "Bad Request",
                "detail": "Missing 1 required argument: 'u_id'"
              }
            ]
          }), 400)

      request_body = request.get_json()
      updated_user = self.user_service.edit_user(u_id, request_body)

      if not updated_user:
        return make_response(jsonify({
            'errors': [
              {
                "status": 404,
                "source": { "pointer": "/profile/<u_id>", "method": "PUT" },
                "title": "User not found",
                "detail": "User with u_id = %s is not found" % (u_id)
              }
            ]
          }), 404)

      response = {
        'message': 'User data is successfully updated!',
        'data': {
          'user': self.user_schema.dump(updated_user)
        }
      }
      return response
    except Exception as e:
      return make_response(jsonify({
        'errors': [
          {
            "status": 500,
            "source": { "pointer": "/profile/", "method": "PUT" },
            "title": "Internal Server Error",
            "detail": str(e)
          }
        ]
      }), 500)