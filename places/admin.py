from django.contrib import admin
from .models import Destination, SpecialDestination, TouristPlaces
# Register your models here.
admin.site.register(Destination)
admin.site.register(SpecialDestination)
admin.site.register(TouristPlaces)


