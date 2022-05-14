from django.views.generic import TemplateView

from jonse.models import Listing


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listing_list"] = Listing.objects.all()
        return context
