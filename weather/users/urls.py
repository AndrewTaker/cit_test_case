from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import SignUpView

app_name = 'users'

urlpatterns = [
    path(
        route='login/',
        view=LoginView.as_view(template_name='users/auth/login.html'),
        name='login'
    ),
    path(
        route='logout/',
        view=LogoutView.as_view(template_name='users/auth/logout.html'),
        name='logout'
    ),
    path(
        route='signup/',
        view=SignUpView.as_view(template_name='users/auth/signup.html'),
        name='signup'
    ),
]
