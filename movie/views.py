from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from .models import Movie
from .forms import AddMovieForm


@method_decorator(login_required(login_url='/'), name='dispatch')
class IndexView(generic.ListView):
    template_name = 'movie/index.html'
    context_object_name = 'all_movies'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user).order_by('-seen_for_the_first_time')


@method_decorator(login_required(login_url='/'), name='dispatch')
class DetailView(generic.DetailView):
    model = Movie
    template_name = 'movie/detail.html'

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)


@method_decorator(login_required(login_url='/'), name='dispatch')
class MovieCreate(CreateView):
    form_class = AddMovieForm
    model = Movie


@method_decorator(login_required(login_url='/'), name='dispatch')
class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie:index')
