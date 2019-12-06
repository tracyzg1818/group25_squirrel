from django.forms import ModelForm 
from sightings.models import show

class SquirrelForm(ModelForm): 
    class Meta: 
        model = show 
        fields = '__all__'     #All fields of squirrels are available in the form
