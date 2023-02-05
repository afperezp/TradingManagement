from django.urls import path
from .views import *



urlpatterns = [
    #ENDPOINTS FOR AssetsManagement
    path('get-all-data/', get_all_movements_clients, name='get_all_movements_clients'),
]