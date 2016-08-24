from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='home'),
    url(r'^registration/$', views.RegistrationPageView.as_view(), name='registration'),
    url(r'^signout/$', views.SignOut.as_view(), name='signout')
]