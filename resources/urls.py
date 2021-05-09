from django.urls import path

from resources import views

urlpatterns = [
    path('', views.resources_view, name='resources'),
]
