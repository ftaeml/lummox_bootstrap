from django.conf.urls import url
from django.contrib import admin
from info import views

urlpatterns = [
    url(r'^contact$', views.contact, name='contact'),
    url(r'^about$', views.about, name="about"),
    ]