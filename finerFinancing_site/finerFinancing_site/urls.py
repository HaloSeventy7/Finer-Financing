# filename: finerFinancing_site/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mainMenu/', include('mainMenu.urls')),
    path('admin/', admin.site.urls),
]
