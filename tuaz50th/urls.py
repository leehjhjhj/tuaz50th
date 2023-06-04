
from django.contrib import admin
from django.urls import path, include
from supply import views
from guestbook import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.balloon_list, name='home'),
    
    path('item/', include('item.urls')),
    path('buy/', include('supply.urls')),
    path('about/', about, name='about'),
    path('blockgame/', blockgame, name='blockgame'),
    path('intro/', intro, name='intro'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)