from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #ENDPOINTS FOR Token JWT
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ENDPOITNS FOR USERS
    path('users/', get_all_users, name ="get_all_users"),
    path('users/<int:pk>/', get_user, name ="get_user"),
    path('users/add-user', create_user, name ="create_user"),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update-profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout')
]