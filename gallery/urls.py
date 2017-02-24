from django.conf.urls import url
from django.contrib import admin
from gallery import views

urlpatterns = [
    url(r'^$', views.gallery, name='home'),
    url(r'^photos/(?P<id>\d+)?$', views.album, name="album"),
    url(r'^albums/(?P<id>\d+)?$', views.albums, name="albums"),
]