from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index, name='home'),
    path('getsnipte/',GetSnipte.as_view(),name='getsnipte'),

]