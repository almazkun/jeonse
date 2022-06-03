from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.accounts.forms import CustomUserCreationForm


# Create your views here.
class SignupView(CreateView):
    template_name = "accounts/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("signin")


class SigninView(views.LoginView):
    template_name = "accounts/signin.html"
    success_url = reverse_lazy("home")


class SignoutView(views.LogoutView):
    success_url = reverse_lazy("home")
