from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .models import Destination, TouristPlaces
from django.views.generic.list import ListView

urlpatterns = [
    path('newuser', views.NewUser.as_view(), name='createuser'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('home', views.HomePageView.as_view(), name='index'),
    # path('dlist', ListView.as_view( model = Destination, template_name = 'places/Destinationlist.html'), name='destinationlist'),
    path('dlist', views.DestinationListView.as_view(), name='destinationlist'),
    path('Tourlist', views.TouristListView.as_view(), name='Touristplaces'),
    path('FormforDestination', views.DestinationCreateView.as_view(), name='DestinationForm'),
    path('FormforTouristplaces', views.TouristPlacesCreateView.as_view(), name='TouristplacesForm'),
    path('Destination_update/<int:pk>', views.DestinationUpdateView.as_view(), name='Destination_update'),
    path('Destination_delete/<int:pk>', views.DestinationDeleteview.as_view(), name='Destination_delete'),


]
