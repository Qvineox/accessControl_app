from django.urls import path

from accounts import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile_view, name='profile'),
    path('profile:<int:profile_id>', views.profile_view, name='profile'),
    path('add_profile', views.add_profile, name='add_profile'),
    path('profiles', views.profiles_view, name='profiles'),
]
