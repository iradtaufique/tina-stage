from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('finance', finance, name='finance'),
    path('profile', profile, name='profile'),
    path('create-stock', createStock, name='create_stock'),
    path('create-item', createItem, name='create_item'),
    path('all-stock', ListAllStock.as_view(), name='all_stock'),
    path('update-stock/<int:pk>', updateStock, name='update_stock'),
    path('laptop-list', laptopList, name='all_laptop'),

]
