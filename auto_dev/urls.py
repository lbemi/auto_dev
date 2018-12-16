"""auto_dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include, handler404, handler500
from django.contrib import admin
import u_app.views as View

handler404 = "u_app.views.page_error"
handler500 = "u_app.views.page_not_found"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('u_app.urls')),
]
