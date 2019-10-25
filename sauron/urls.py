from django.urls import path, include, re_path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', SauronTemplateView.as_view(), name='sauron'),
    url('upload', upload_xlsx, name='upload'),
    # url('r^/', background_view, name='background_view')
]