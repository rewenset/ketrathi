from django.conf.urls import url
from . import views

app_name = 'movie'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^movie/add/$', views.MovieCreate.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.MovieDelete.as_view(), name='delete'),
]