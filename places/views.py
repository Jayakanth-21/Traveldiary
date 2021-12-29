from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Destination, TouristPlaces


def index(request):
    return HttpResponse("Hello, world!. You're at the polls index.")


class HomePageView(TemplateView):

    template_name = "places/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant']='Traveldiary'
        print(Destination.objects.all())  # Fetches all the records from the database of destination model
        return context


class DestinationListView(ListView):

    model = Destination
    template_name = 'places/mylist.html'


class TouristListView(ListView):

    model = TouristPlaces
    template_name = 'places/display_touristplaces.html'
