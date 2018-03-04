"""定义learning_logs的URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
#    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
#    url(r'^new_topic/$', views.new_topic, name='new_topic'),
#   url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
#    path('',views.index, name='index')
#    path('topics/',views.topics,name='topics'),
]
