from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Clients, Trader

User = get_user_model()
admin.site.register(User)
admin.site.register(Trader)
admin.site.register(Clients)