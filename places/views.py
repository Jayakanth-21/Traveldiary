from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Destination, TouristPlaces
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import DestinationForm, Register
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count, Min, Sum
from django.contrib import messages
import pycountry
import requests


def index(request):

    return HttpResponse("Hello, world!. You're at the polls index.")


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "places/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['variant'] = 'Traveldiary'
        # print(Destination.objects.all())  # Fetches all the records from the database of destination model
        return context


class DestinationListView(ListView):
    # model = Destination
    template_name = 'places/Destinationlist.html'

    def get_queryset(self):
        # Are we overriding it by calling with the default name
        traveller_specific = Destination.objects.filter(traveller=self.request.user)
        return traveller_specific

    def get_context_data(self, **kwargs):
        """ the purpose of using this method is to display the additional data in template page"""
        context = super().get_context_data(**kwargs)
        # method 1: Using aggregation from Django.
        total_budget = Destination.objects.filter(traveller=self.request.user).aggregate(total_budget=Sum('budget'))
        context['total_budget'] = total_budget["total_budget"]
        # Weather API
        traveller_specific = Destination.objects.filter(traveller=self.request.user).values()
        # The above line is a query set and converts it to dictionary.
        API_KEY = '827679da6377f92463b229860c4a2792'

        for tr in traveller_specific:
            payload = {
                'q': tr['name_of_the_place'],
                'appid': API_KEY,
                'units': 'metric',
            }

            url1 = 'http://api.openweathermap.org/data/2.5/weather'
            r1 = requests.get(url1, params=payload)
            my_dict = r1.json()
            # print(tr)
            try:
                tr['temp'] = my_dict['main']['temp']
            except:
                tr['temp'] = 0

        for tr in traveller_specific:
            print(tr)

        # print(my_dict)
        # print(my_dict['weather'])
        # print(my_dict['name'])
        # print(my_dict['main']['temp'])

        # weather_dict = {
        #     'city_name': my_dict['name'],
        #     'city_temp': my_dict['main']['temp']
        #
        # }
        # context['weather_dict']= weather_dict

        context["city_weather"] = traveller_specific
        return context
        # Method 2: Using for loop
        # traveller_specific = Destination.objects.filter(traveller=self.request.user)
        # budget = 0
        # for cost in traveller_specific:
        #     budget += cost.budget
        # context['total_budget'] = budget
        # return context


class TouristListView(ListView):
    model = TouristPlaces
    template_name = 'places/display_touristplaces.html'

    def get_queryset(self):
        """ get_queryset is a default Django method which fetches all the available particular model data from the database. """

        # qs = super().get_queryset()
        # for q in qs:
        #     print(q)
        #     Django template language can only be use with template files
        # traveller_specific = TouristPlaces.objects.filter(traveller=self.request.user)
        traveller_specific = TouristPlaces.objects.filter(destination__traveller=self.request.user)
        return traveller_specific


class DestinationCreateView(CreateView):
    form_class = DestinationForm
    model = Destination
    # fields = ['name_of_the_place','budget', 'why_this_place', 'already_visited','add_field']
    # fields = '__all__' (It displays all the fields inside the class")
    success_url = reverse_lazy('index')

    def get_initial(self):
        data = {'traveller': self.request.user}
        return data

    def form_valid(self, form):

        Repeated_dest = Destination.objects.filter(traveller=self.request.user,
                                                   name_of_the_place=form.cleaned_data['name_of_the_place']).exists()
        if Repeated_dest:
            messages.warning(self.request, 'Repeated Destinations are not valid to enter')
            return HttpResponseRedirect(reverse_lazy('DestinationForm'))

        # why is this giving only name_of_the_place objects

        #     print (dest)
        # print(form.cleaned_data['name_of_the_place'])
        #
        # # print (Repeated_dest)
        # for dest in Repeated_dest:
        #     if form.cleaned_data['name_of_the_place'] == dest.name_of_the_place:
        #         messages.warning(self.request, 'Repeated Destinations are not valid to enter')
        #         return HttpResponseRedirect(reverse_lazy('DestinationForm'))

        t_count = Destination.objects.filter(traveller=self.request.user).count()

        if t_count >= 10:
            print("only 10 allowed")
            messages.warning(self.request, 'Only 10 Destinations allowed.')
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            return super().form_valid(form)


class TouristPlacesCreateView(CreateView):
    model = TouristPlaces
    fields = ['name_of_tourist_place', 'destination', 'traveller']
    template_name = 'places/Touristplacesform.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
        data = {'traveller': self.request.user}
        return data

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


class DestinationDeleteview(DeleteView):
    model = Destination
    success_url = reverse_lazy('destinationlist')


class NewUser(FormView):
    form_class = Register
    template_name = 'places/user_registration.html'

    # success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        print(username)
        return HttpResponseRedirect(reverse_lazy('login'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))
