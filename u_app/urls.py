from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login),
    url(r'^logout/$',views.logout, name='logout'),
    url(r'^index/', views.login, name='index'),
    url(r'^host/serverlist/$', views.serverList, name='server_list'),
    url(r'^host/serverlist/(.+)/$', views.serverList, name='server_delete'),
    url(r'^host/serveradd/$', views.server_add, name='server_add'),
    url(r'^host/exec/(.+)/$', views.exec_cmd, name='exec_cmd'),
    url(r'^host/exec/$', views.exec_cmd, name='exec_q'),
    url(r'^api/method=exe$', views.api, name='api'),
]