from django.forms import ModelForm
from .models import Car

class CarForm(ModelForm):
  class Meta:
    model = Car
    fields = ['date', 'challenge', 'action', 'response']