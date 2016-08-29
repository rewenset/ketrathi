from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Movie(models.Model):
    user = models.ForeignKey(User, default=1)
    original_title = models.CharField(max_length=200)
    seen_for_the_first_time = models.DateField()
    poster = models.FileField()
    imdbRating = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('movie:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        import urllib.request
        import json
        title = str(self.original_title)
        title = title.replace(" ", "+")
        url = 'http://www.omdbapi.com/?t={}&y=&plot=short&r=json'.format(title)
        url = url.replace(' ', '+')
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()
        data = json.loads(resp_data.decode('utf-8'))
        self.imdbRating = data['imdbRating']
        super(Movie, self).save(*args, **kwargs)
