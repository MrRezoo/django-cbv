from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login')
    # path('logout/', auth_views.LogoutView.as_view(next_page='first:home'), name='logout'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/', views.UserPassReset.as_view(), name='reset_pass'),
    path('reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('confirm/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
]