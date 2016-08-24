from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Movie(models.Model):
    user = models.ForeignKey(User, default=1)
    original_title = models.CharField(max_length=500)
    seen_for_the_first_time = models.DateField()
    poster = models.FileField()

    def get_absolute_url(self):
        return reverse('movie:detail', kwargs={'pk': self.pk})
