from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('delorean/', DeloreanTemplateView.as_view(), name='delorean'),
]
