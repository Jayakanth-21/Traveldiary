from django.forms import ModelForm
from .models import Destination, TouristPlaces
from django import forms

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']='form-control'

        self.fields['name_of_the_place'].widget.attrs['autofocus']='autofocus'
        self.fields['traveller'].widget = forms.HiddenInput()