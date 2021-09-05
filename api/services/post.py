import uuid
from api.models.post import PostModel
from api.utils import db

class PostService:

  def get_all_posts(self):
    posts = PostModel.query.all()
    return posts

  def get_post_by_id(self, p_id):
    post = PostModel.query.filter_by(p_id=p_id).first()
    return post

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

  def edit_post(self, p_id, request_body):
    post = PostModel.query.filter_by(p_id=p_id).first()
    if not post:
      return None
    
    if 'p_title' in request_body:
      post.p_title = request_body['p_title']
    if 'p_subtitle' in request_body:
      post.p_subtitle = request_body['p_subtitle']
    if 'p_content' in request_body:
      post.p_content = request_body['p_content']
    if 'p_cover' in request_body:
      post.p_cover = request_body['p_cover']
    if 'p_status' in request_body:
      post.p_status = request_body['p_status']
    if 'p_updated_at' in request_body:
      post.p_updated_at = request_body['p_updated_at']
    if 'p_published_at' in request_body:
      post.p_published_at = request_body['p_published_at']
    
    db.session.commit()
    return post
  
  def delete_post(self, p_id):
    post = PostModel.query.filter_by(p_id=p_id).first()
    if not post:
      return None
    
    post_title = post.p_title
    
    db.session.delete(post)
    db.session.commit()
    return {
      "p_title": post_title
    }