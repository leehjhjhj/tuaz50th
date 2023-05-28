
from django.contrib import admin
from django.urls import path
from supply import views
from guestbook import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.balloon_list, name='home'),
]
