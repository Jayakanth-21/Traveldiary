from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Destination, TouristPlaces
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


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
    template_name = 'places/Destinationlist.html'




class TouristListView(ListView):

    model = TouristPlaces
    template_name = 'places/display_touristplaces.html'


class DestinationCreateView(CreateView):

    model = Destination
    fields = ['name_of_the_place','budget', 'why_this_place', 'already_visited','add_field']
    # fields = '__all__' (It displays all the fields inside the class")
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        t_count = Destination.objects.count()
        if t_count >= 10:
            print("only 10 allowed")

        else:
            return super().form_valid(form)




class TouristPlacesCreateView(CreateView):

    model = TouristPlaces
    fields = ['name_of_tourist_place','destination']
    template_name = 'places/Touristplacesform.html'
    success_url = reverse_lazy('TouristplacesForm')




    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     super().post(request, *args, **kwargs)
    #     return render(request,'places/Touristplacesform.html')


class DestinationUpdateView(UpdateView):

    model = Destination
    fields = '__all__'
    # template_name_suffix = '_update_form' (The UpdateView page displayed to a GET request uses a template_name_suffix of '_form')
    template_name = 'places/Destination_update_form.html'
    success_url = reverse_lazy('index')