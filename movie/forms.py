from django import forms
from datetime import date
from .models import Movie


class AddMovieForm(forms.ModelForm):
    seen_for_the_first_time = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'))

    class Meta:
        model = Movie
        fields = ['original_title', 'seen_for_the_first_time', 'poster']