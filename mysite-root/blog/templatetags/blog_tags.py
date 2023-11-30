from django import template

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    # Возвращает число опубликованных в блоге постов
    return Post.published.count()
