from django.shortcuts import render
from .models import Resume
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse




class NewResume(View):
    def get(self, request):
        return render(request, 'resume/ResumeCreation.html')

    def post(self, request):
        desc = request.POST.get('description')
        Resume.objects.create(author=request.user, description=desc)
        return redirect('/home')


class ResumeView(View):

    def get(self, request):
        resumes = Resume.objects.all()
        return render(request, 'resume/resumeView.html', context={'resumes': resumes})
# Create your views here.
