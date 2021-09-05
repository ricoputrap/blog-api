import uuid
from api.models.post import PostModel
from api.utils import db

class PostService:

  def get_all_posts(self):
    posts = PostModel.query.all()
    return posts

  def create_new_post(self, new_post_data):
    p_id = str(uuid.uuid4())
    
    p_subtitle = ""
    if "p_subtitle" in new_post_data:
      p_subtitle = new_post_data['p_subtitle']
    
    p_cover = ""
    if "p_cover" in new_post_data:
      p_cover = new_post_data['p_cover']
    
    new_post = PostModel(
      p_id = p_id,
      p_title = new_post_data['p_title'],
      p_subtitle = p_subtitle,
      p_content = new_post_data['p_content'],
      p_cover = p_cover,
      p_creator = new_post_data['p_creator'],
    )
    db.session.add(new_post)
    db.session.commit()
    return new_post