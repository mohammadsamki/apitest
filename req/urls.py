from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('home/', index, name='home'),
    path('getsnipte/',GetSnipte.as_view(),name='getsnipte'),
    path('postsnipte/',PostSnipte.as_view(),name="postsnipte"),
    path('updatesnipte/<int:pk>/',UpdateSnipte.as_view(),name='updatesnipte'),
    path('deletesnipte/<int:pk>/',DeleteSnipte.as_view(),name='deletesnipte'),

]
