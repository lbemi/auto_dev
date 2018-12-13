from django.conf.urls import url
from . import views
import os
import time

urlpatterns = [
    url(r'^$', views.index, name='index'),

]