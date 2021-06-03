
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("authentication/", include("authentication.urls")),
    path("", include("core.urls")),
    path("", include("library.urls")),
]
