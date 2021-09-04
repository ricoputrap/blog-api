from api.utils import ma

class PostSchema(ma.Schema):
  class Meta:
    fields = (
      "p_id",
      "p_title",
      "p_subtitle",
      "p_content",
      "p_cover",
      "p_creator",
      "p_status",
      "p_created_at",
      "p_updated_at",
      "p_published_at"
    )