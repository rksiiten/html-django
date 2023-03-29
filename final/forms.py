from django import forms
from .models import Person

# creating a form
class PersonForm(forms.ModelForm):
  
    # create meta class
    class Meta:
        # specify model to be used
        model = Person
        fields = '__all__'