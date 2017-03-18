from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^write-blog/$', views.write_blog),
    url(r'^get-blogs/$', views.get_blogs),
    url(r'^write-comment/(?P<para_id>\d+)/$', views.write_comment),
    url(r'^get-comments/(?P<blog_id>\d+)/$', views.get_comments),
]

