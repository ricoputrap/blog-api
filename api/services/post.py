from api.models.post import PostModel

class PostService:

  def get_all_posts(self):
    posts = PostModel.query.all()
    return posts