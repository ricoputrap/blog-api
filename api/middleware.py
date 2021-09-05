import os
from dotenv import load_dotenv
load_dotenv()

from werkzeug.wrappers import Request, Response
from jwt.exceptions import ExpiredSignatureError, InvalidKeyError
import json
import jwt

class AuthMiddleware:

  auth_token_not_provided = { "message": "Authentication credentials were not provided." }
  auth_token_not_valid = { "message": "Authentication token is not valid." }
  auth_token_expired = { "message": "Authentication token has expired." }

  def __init__(self, app):
    self.app = app
  
  def __call__(self, environ, start_response):
    res = Response(mimetype='application/json', status=401)
    req = Request(environ)
    path = req.path.split('/')[1]
    method = req.method

    is_edit_profile = path == 'profile' and method == 'PUT'
    is_add_post = path == 'posts' and method == 'POST'
    is_edit_post = path == 'posts' and method == 'PUT'
    is_delete_post = path == 'posts' and method == 'DELETE'
    is_need_auth = is_edit_profile or is_add_post or is_edit_post or is_delete_post

    if is_need_auth:
      try:
        header_auth = req.headers['Authorization']
        auth_token = header_auth.replace('Bearer ', '')
        secret_key = os.getenv('SECRET_KEY')
        jwt.decode(auth_token, secret_key, algorithms=['HS256'])
        
        return self.app(environ, start_response)

      except ExpiredSignatureError as e:
        res.data = json.dumps(self.auth_token_expired)
        return res(environ, start_response)
      
      except InvalidKeyError as e:
        res.data = json.dumps(self.auth_token_not_valid)
        return res(environ, start_response)

      except KeyError as e:
        res.data = json.dumps(self.auth_token_not_provided)
        return res(environ, start_response)

      except Exception as e:
        res.data = json.dumps(self.auth_token_not_provided)
        return res(environ, start_response)

    return self.app(environ, start_response)    