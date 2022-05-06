from Account.views import (registration_view, )
from django.urls import path

app_name = 'account_app'

urlpatterns = [
    path('register/', registration_view, name='register'),
]
