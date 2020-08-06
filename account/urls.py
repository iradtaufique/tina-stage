from django.urls import path
from .views import *

urlpatterns = [
    path('SignUp', signUp, name='signUp'),
    path('create-user', createUser, name='create'),


]
