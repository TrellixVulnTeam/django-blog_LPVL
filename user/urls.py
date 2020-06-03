from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    # ! loginView and logoutView
    path('login/', LoginView.as_view(template_name='login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='logout.html'),
         name='logout'),
    # ! login and logout form
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),

    #     ! profile
    path('profile/', views.profile, name='profile'),
]