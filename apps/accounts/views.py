from django.views.generic import FormView

from apps.accounts.forms import CustomUserCreationForm


# Create your views here.
class SignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = CustomUserCreationForm
    success_url = "/"

    def form_valid(self, form):
        request = self.request
        next_path = request.GET.get("next")
        return redirect(next_path)


class SigninView(FormView):
    pass


class SignoutView(FormView):
    pass
