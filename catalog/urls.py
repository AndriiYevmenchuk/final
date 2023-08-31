from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index),
    re_path(r'^details/(?P<product_id>[0-9]+)$', details),
]
