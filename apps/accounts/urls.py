from django.urls import path

from apps.accounts.views import SigninView, SignoutView, SignupView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("signin/", SigninView.as_view(), name="signin"),
    path("signout/", SignoutView.as_view(), name="signout"),
]
