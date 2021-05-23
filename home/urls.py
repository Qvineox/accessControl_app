from django.urls import path

from home import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('entries', views.entries_view, name='entries'),
    path('filter_entries', views.filter_entries, name='filter_entries'),
    path('add_entry', views.add_entry, name='add_entry'),
    path('entry/<int:entry_id>', views.entry_view, name='entry'),
]
