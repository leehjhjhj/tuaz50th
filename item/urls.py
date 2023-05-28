from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'item'

urlpatterns = [
    path('', all_items, name='all'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 코드 추가!
