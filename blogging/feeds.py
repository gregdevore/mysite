from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post

class LatestPostsFeed(Feed):
    title = 'Latest Blog Posts'
    link = '/blogging/'
    description = 'Latest blogs from our users'

    def items(self):
        return Post.objects.exclude(published_date__exact=None).order_by('-published_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
