from api.utils import db

class PostModel(db.Model):
  __tablename__ = 'post'
  p_id = db.Column(db.String(50), primary_key=True)
  p_title = db.Column(db.String(50), nullable=False)
  p_subtitle = db.Column(db.String(255), nullable=True)
  p_content = db.Column(db.Text, nullable=False)
  p_cover = db.Column(db.Text, nullable=True)
  p_creator = db.Column(db.String(50), db.ForeignKey('user.u_id'), nullable=False)
  p_status = db.Column(db.String(4), nullable=False, default='DRFT')
  p_created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
  p_updated_at = db.Column(db.DateTime, nullable=True)
  p_published_at = db.Column(db.DateTime, nullable=True)