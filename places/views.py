from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Destination, TouristPlaces
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import DestinationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect

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

    def get_queryset(self):
        traveller_specific = Destination.objects.filter(traveller=self.request.user)
        return traveller_specific


class TouristListView(ListView):

    model = TouristPlaces
    template_name = 'places/display_touristplaces.html'


class DestinationCreateView(CreateView):

    form_class = DestinationForm
    model = Destination
    # fields = ['name_of_the_place','budget', 'why_this_place', 'already_visited','add_field']
    # fields = '__all__' (It displays all the fields inside the class")
    success_url = reverse_lazy('index')


    def get_initial(self):
        data = {'traveller':self.request.user}
        return data
    # def form_valid(self, form):
    #     t_count = Destination.objects.count()
    #     if t_count >= 10:
    #         print("only 10 allowed")
    #
    #     else:
    #         return super().form_valid(form)

class TouristPlacesCreateView(CreateView):

    model = TouristPlaces
    fields = ['name_of_tourist_place','destination']
    template_name = 'places/Touristplacesform.html'
    success_url = reverse_lazy('TouristplacesForm')

def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))





    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     super().post(request, *args, **kwargs)
    #     return render(request,'places/Touristplacesform.html')


class DestinationUpdateView(UpdateView):

    model = Destination
    fields = ['name_of_the_place', 'budget', 'why_this_place', 'already_visited', 'add_field']

    # template_name_suffix = '_update_form' (The UpdateView page displayed to a GET request uses a template_name_suffix of '_form')
    template_name = 'places/Destination_update_form.html'
    success_url = reverse_lazy('index')

class DestinationDelteview(DeleteView):

    model = Destination
    success_url = reverse_lazy('destinationlist')