from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('resources/', include('resources.urls')),
]
