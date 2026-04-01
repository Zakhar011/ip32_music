from django import forms
from .models import Janri,Track, Artist
 
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
class ArtistForm(forms.ModelForm):
    class Meta:
        model=Artist
        fields = '__all__'
        labels = {
            'name': 'Имя/название',
            'image': 'Фотография',
        }        