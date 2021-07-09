from django.urls import path

from . import views
from django.contrib.auth import views as av

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('user_profile/<int:user_pk>/', views.user_profile, name='user_profile'),
    path('follow/<int:user_pk>/', views.follow,name='follow'),
    path('create/', views.create_account, name='create_account'),
    path('change_data/', views.change_data, name='change_data'),
    path('login/', av.LoginView.as_view(), name='login'),
    path('logout/', av.LogoutView.as_view(), name='logout'),
    path('password_change/', av.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', av.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', av.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', av.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset///', av.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', av.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile_edit/', views.ProfileEditView.as_view(), name='profile_edit'),
]