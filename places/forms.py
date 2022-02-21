from django.forms import ModelForm
from .models import Destination, TouristPlaces
from django import forms
from django.contrib.auth.forms import UserCreationForm
import pycountry



class DestinationForm(ModelForm):
    class Meta:


        model = Destination
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['name_of_the_place'].widget.attrs['autofocus'] = 'autofocus'
        self.fields['traveller'].widget = forms.HiddenInput()

    # def clean(self):
    #     cleaned_data=self.cleaned_data
    #     # if cleaned_data["budget"]>10000 or cleaned_data["budget"] <=0:
    #     # if not 0< cleaned_data["budget"] <=10000:
    #     #     raise forms.ValidationError("The budget should be below 10,000")
    #     if budget_range(cleaned_data["budget"]):
    #
    #         raise forms.ValidationError("The budget should be below 10,000")
    #     return self.cleaned_data



    def clean(self):
        # Does clean take only one argument
        # By using clean method, are we by default asking to validate the field
        # what is cleaned_data

        cleaned_data=self.cleaned_data
        # if cleaned_data["budget"]>10000 or cleaned_data["budget"] <=0:
        # if not 0< cleaned_data["budget"] <=10000:
        #     raise forms.ValidationError("The budget should be below 10,000")
        if valid_country(cleaned_data["name_of_the_place"]):
            raise forms.ValidationError("The country name should be a valid one")

        if budget_range(cleaned_data["budget"]):
            raise forms.ValidationError("The budget should be below 10,000")

        # return self.cleaned_data

        return self.cleaned_data


class Register(UserCreationForm):

      pass

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'


def budget_range(user_budget):

    if not 0 < user_budget <= 10000:
        return True
    else:
        return False

# budget_range(2000)

# list_of_countries = {"India","china","England","America","canada"}
# country_names = list()
#         for c in country_names:
#             print(c.name)
def valid_country(country_name):

    for country in pycountry.countries:
       if country_name.upper() == country.name.upper():
           return False

    else:
        return True
       # False means the function is not really doing anything when called with 'if' in the above.
       # else:
       #     print(country_name)
       #     print(country)
       #     return True

# print(pycountry.countries)







