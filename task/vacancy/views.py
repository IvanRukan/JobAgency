from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Vacancy
from django.views import View
from django.contrib.auth.models import User


class NewVacancy(View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, 'vacancy/VacancyCreation.html')
        else:
            return HttpResponse(status=403)

    def post(self, request):
        if request.user.is_staff:
            desc = request.POST.get('description')
            Vacancy.objects.create(author=request.user, description=desc)
            return redirect('/home')
        else:
            return HttpResponse(status=403)


class VacancyView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy/vacancyView.html', context={'vacancies': vacancies})
