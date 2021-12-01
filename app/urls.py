from django.urls import path
from .views import *

urlpatterns = [
    path('sample/', HelloView.as_view(), name='sample'),
    path('register/', UserCreate.as_view(), name='userdata'),
]