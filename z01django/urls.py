from django.contrib import admin
from django.urls import path, include
from app.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('main/', main, name="main"),
]
