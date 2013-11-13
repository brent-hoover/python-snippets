from django.conf.urls import patterns, url
from views import BlogPostDetailView

urlpatterns = patterns('',
    url(r'^(?P<post_slug>.*)', BlogPostDetailView.as_view(), {}, 'post-view'),
)

