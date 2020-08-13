from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'app', views.index, name='index'),
    url(r'^get_user_activity/$', views.UserList.as_view()),
]