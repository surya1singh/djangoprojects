from django.forms import CharField, ModelForm
from .models import Animals

class AnimalsForm(ModelForm):
    class Meta:
        model = Animals
        fields = ['title', 'content']
