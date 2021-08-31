from api.utils import db

class PostModel(db.Model):
  __tablename__ = 'Post'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  subtitle = db.Column(db.String(255), nullable=True)
  content = db.Column(db.Text, nullable=False)
  cover_picture = db.Column(db.Text, nullable=True)
  creator = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
  status = db.Column(db.String(4), nullable=False, default='DRFT')
  created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, nullable=True)
  published_at = db.Column(db.DateTime, nullable=True)