from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'supply'

urlpatterns = [
    path('', buy, name='buy'),
    path('create/', create, name='create')
]