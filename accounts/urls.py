from django.urls import path

from accounts import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile_view, name='profile'),
    path('division:<int:division_id>', views.division_view, name='division'),
    path('profile:<int:profile_id>', views.profile_view, name='profile'),
    path('add_profile', views.add_profile, name='add_profile'),
    path('add_division', views.add_division, name='add_division'),
    path('profiles', views.profiles_view, name='profiles'),
]
