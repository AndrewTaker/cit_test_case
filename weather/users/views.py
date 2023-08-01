from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import CreateUserForm


class SignUpView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/auth/signup.html'
