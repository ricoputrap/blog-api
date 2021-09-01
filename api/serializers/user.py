from api.utils import ma

class UserSchema(ma.Schema):
  class Meta:
    fields = (
      "u_id",
      "u_username",
      "u_email",
      "u_fullname",
      "u_occupation"
    )