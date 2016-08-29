from django import forms
from datetime import date
from .models import Movie


class AddMovieForm(forms.ModelForm):
    seen_for_the_first_time = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'))

    class Meta:
        model = Movie
        fields = ['original_title', 'seen_for_the_first_time', 'poster']


    def clean(self):
        import urllib.request
        import json
        cleaned_data = super(AddMovieForm, self).clean()
        title = cleaned_data.get('original_title')
        title = title.replace(' ', '+')
        url = 'http://www.omdbapi.com/?t={}&y=&plot=short&r=json'.format(title)
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()

        data = json.loads(resp_data.decode('utf-8'))

        if 'Error' in data.keys():
            print(data['Error'])
            raise forms.ValidationError(data['Error'])

        return cleaned_data