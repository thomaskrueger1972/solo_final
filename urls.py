from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('albums', views.albums),
    path('create_album', views.create_album),
    path('upload', views.upload),
    path('back', views.back),
    path('media/images', views.media)
    ]