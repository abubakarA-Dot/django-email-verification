from django.urls import path
from .views import (
    home_view, sign_up, login, token_sent
)

urlpatterns = [
    path('', home_view, name = 'home_view'),
    path('accounts/sign-up/', sign_up, name='sign-up'),
    path('accounts/login/', login, name='login'),
    path('token/sent/', token_sent, name='sent_token'),
]
