from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('dlist', views.DestinationListView.as_view(), name='destinationlist'),
    path('Tourlist', views.TouristListView.as_view(), name='Touristplaces'),
    path('FormforDestination', views.DestinationCreateView.as_view(), name='DestinationForm'),
    path('FormforTouristplaces', views.TouristPlacesCreateView.as_view(), name='TouristplacesForm'),

]