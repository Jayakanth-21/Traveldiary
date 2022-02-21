from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name_of_the_place = models.CharField(max_length=25)
    budget = models.IntegerField(default=10)
    why_this_place = models.TextField(max_length = 1000)
    already_visited = models.BooleanField(default=False)
    add_field = models.CharField(max_length=10, default='and')
    traveller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_of_the_place



class TouristPlaces(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name_of_tourist_place = models.CharField(max_length=25)
    traveller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name_of_tourist_place

class SpecialDestination(Destination):
    restricted_area = models.BooleanField(default=True)



