from flask import make_response, jsonify, request
from flask_restful import Resource
from api.services.post import PostService
from api.serializers.post import PostSchema

class Post(Resource):

  post_service = PostService()
  post_schema = PostSchema()
  post_list_schema = PostSchema(many=True)

  def get(self, p_id = None):
    try:
      if p_id == None:
        posts = self.post_service.get_all_posts()
        response = {
          'message': "Get all posts is success!",
          'data': {
            'posts': self.post_list_schema.dump(posts),
            'total': len(posts)
          }
        }
      else:
        response = ""
      #   user = self.post_service.get_user_by_id(p_id)

      #   if not user:
      #     return make_response(jsonify({
      #       'errors': {
      #         'status': 404,
      #         'title': 'User not found',
      #         'detail': 'User with p_id = %s is not found' % (p_id),
      #         'source': {
      #           'pointer': '/profile/<p_id>',
      #           'method': 'GET'
      #         },
      #       }
      #     }), 404)
        
      #   response = {
      #     'message': 'Get user by p_id is success!',
      #     'data': {
      #       'user': self.user_schema.dump(user),
      #     }
      #   }
      return response
    except Exception as e:
      return make_response(jsonify({
        'errors': [
          {
            "status": 500,
            "source": { "pointer": "/posts/", "method": "GET" },
            "title": "Internal Server Error",
            "detail": str(e)
          }
        ]
      }), 500)

  def post(self):
    try:
      request_body = request.get_json()
      new_post = self.post_service.create_new_post(request_body)
      response = {
        "message": "New post is successfully created!",
        "data": {
          "post": self.post_schema.dump(new_post)
        }
      }
      return response
    except Exception as e:
      return make_response(jsonify({
        "errors": [
          {
            "status": 500,
            "source": { "pointer": "/posts/", "method": "POST" },
            "title": "Internal Server Error",
            "detail": str(e)
          }
        ]
      }), 500)
  
  # def put(self, u_id = None):
  #   '''
  #   @TODO set error if `request_body` is empty
  #   '''
  #   try:
  #     if not u_id:
  #       return make_response(jsonify({
  #           'errors': [
  #             {
  #               "status": 400,
  #               "source": { "pointer": "/profile/<u_id>", "method": "PUT" },
  #               "title": "Bad Request",
  #               "detail": "Missing 1 required argument: 'u_id'"
  #             }
  #           ]
  #         }), 400)

  #     request_body = request.get_json()
  #     updated_user = self.user_service.edit_user(u_id, request_body)

  #     if not updated_user:
  #       return make_response(jsonify({
  #           'errors': [
  #             {
  #               "status": 404,
  #               "source": { "pointer": "/profile/<u_id>", "method": "PUT" },
  #               "title": "User not found",
  #               "detail": "User with u_id = %s is not found" % (u_id)
  #             }
  #           ]
  #         }), 404)

  #     response = {
  #       'message': 'User data is successfully updated!',
  #       'data': {
  #         'user': self.user_schema.dump(updated_user)
  #       }
  #     }
  #     return response
  #   except Exception as e:
  #     return make_response(jsonify({
  #       'errors': [
  #         {
  #           "status": 500,
  #           "source": { "pointer": "/profile/", "method": "PUT" },
  #           "title": "Internal Server Error",
  #           "detail": str(e)
  #         }
  #       ]
  #     }), 500)