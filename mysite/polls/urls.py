from django.urls import path,include
from . import views

from django.contrib import admin


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]