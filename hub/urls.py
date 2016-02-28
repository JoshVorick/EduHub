from django.conf.urls import url
from . import views

urlpatterns = [
    # Base pages
    url(r'^$', views.index, name='index'),
    url(r'^logout', views.do_logout, name='logout'),
    url(r'^login_check$', views.login_check, name='login_check'),
    # Topic-related
    url(r'^topics$', views.topic_list, name='topic_list'),
    url(r'^topic-nodes$', views.topic_list_jstree, name='topic_list_jstree'),
    url(r'^topic/(?P<pk>\d+)/details.json', views.topic_detail_json, name='topic_detail_json'),
    url(r'^topic/(?P<pk>\d+)/resources.json', views.topic_resource_json, name='topic_resource_json'),
    # Resource
    url(r'^resource/(?P<pk>\d+)/view', views.resource_view, name='resource_view'),
    url(r'^resource/(?P<pk>\d+)/related.json', views.related_resources_json, name='related_resources_json'),
    url(r'^forum/(?P<pk>\d+)/threads.json', views.load_forum_posts, name='load_forum_posts'),
    url(r'^random-resource', views.randomresource_view, name='randomresource')
]
