from django.conf.urls import url
from . import views
import os
import time

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/', views.home_page, name='home_page'),
    url(r'^login', views.login, name='login'),

]