import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        # Выводит 5 последних постов
        return Post.published.all()[:5]

    def item_title(self, item):
        # Вывод заголовок статьи
        return item.title

    def item_description(self, item):
        # Выводит описание статьи обрезая до 30 слов
        return truncatewords_html(markdown.markdown(item.body), 30)

    def item_pubdate(self, item):
        # Выводи дату публикации статьи
        return item.publish
