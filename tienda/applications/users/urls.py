
from unicodedata import name
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'login/',
         views.LoginUser.as_view(), name='login'
    ),
    path('api/google-login/', views.GoogleLoginView.as_view(), name='user-gogole_login')
]