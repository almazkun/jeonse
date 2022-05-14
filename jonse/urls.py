from django.urls import path

from jonse.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
