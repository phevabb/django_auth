from django.urls import path

from .views import ResetAPIView, ForgotAPIView, RefreshAPIView, RegisterAPIView, LoginAPIView, userAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/', userAPIView.as_view(), name='user'),
    path('refresh/', RefreshAPIView.as_view(), name='refresh'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('forgot/', ForgotAPIView.as_view(), name='reset'),
    path('reset/', ResetAPIView.as_view(), name='reset'),
]


    