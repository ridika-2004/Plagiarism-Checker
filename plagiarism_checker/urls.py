from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('checker.urls')),
    path('admin/', admin.site.urls),
]