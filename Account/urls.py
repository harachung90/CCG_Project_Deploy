from Account.views import (registration_view, login_view, logout_view)
from django.urls import path

app_name = 'account_app'

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
]
