from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from .forms import UserForm, RegistrationForm


class IndexPageView(View):
    form_class = UserForm
    template_name = 'home/index.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        context = {
            'form': form,
            'error_message': 'Invalid email address/password combination.'
        }

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:home')

            context['error_message'] = 'Your account has been disabled'

        return render(request, self.template_name, context)
        # form = self.form_class(request.POST)
        # if request.user.is_authenticated():
        #     logout(request)
        #
        # if form.is_valid():
        #     print(5)
        #     # user = form.save(commit=False)
        #
        #     username = form.cleaned_data['username']
        #     password = form.cleaned_data['password']
        #     # user.set_password(password)
        #     # user.save()
        #     user = authenticate(username=username, password=password)
        #     print(6)
        #     if user is not None:
        #         print(7)
        #         if user.is_active:
        #             print(8)
        #             login(request, user)
        #             return redirect('home:chooser')
        # print(form.errors)
        # return render(request, self.template_name, {'form': form})


class RegistrationPageView(View):
    form_class = RegistrationForm
    template_name = 'home/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            password1 = form.cleaned_data['password1']
            user.set_password(password1)
            user.save()
            user = authenticate(username=user.username, password=password1)
            login(request, user)
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')
