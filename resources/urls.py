from django.urls import path

from resources import views

urlpatterns = [
    path('', views.resources_view, name='resources'),
    path('add_resource', views.add_resource, name='add_resource'),
    path('add_facility', views.add_facility, name='add_facility'),
    path('resource/<int:resource_id>', views.resource_view, name='resource'),
]
