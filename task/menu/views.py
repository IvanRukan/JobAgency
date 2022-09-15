from django.shortcuts import render
from django.views.generic import RedirectView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


# Create your views here.


class MenuView(RedirectView):
    def get(self, request, *args, **kwargs):
        return render(request, 'menu/menuView.html')


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'menu/signupView.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'menu/loginView.html'


class HomeView(RedirectView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if User.is_staff:
                return render(request, 'menu/NewVacancy.html')
            else:
                return render(request, 'menu/NewResume.html')
        else:
            return render(request, 'menu/NotLoggedIn.html')





