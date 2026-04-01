from django import forms
from .models import Janri,Track
 
class AddForm(forms.ModelForm):
    class Meta:
        model = Janri
        fields = '__all__'
        labels = {
            'name_ru': 'Название по русски',
            'name_en': 'Название на англ',
            'description': 'Описание',
        }

class AddFormTracks(forms.ModelForm):
    class Meta:
        model =Track
        fields = '__all__'
        labels = {
            'title': 'Название',
            'duration': 'Длительность',
            'name_en': 'Жанр',
        }