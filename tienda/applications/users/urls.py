
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'login/',
         views.LoginUser.as_view(), name='login'
    ),
]