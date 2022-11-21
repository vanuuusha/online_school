from django.shortcuts import render
from django.views import View
from app_students.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'app_students/login.html', {'form': form})

    def post(self, request): #TODO добавить в валидацию проверку на учителя
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
        return HttpResponseRedirect(reverse('students:profile'))


class ProfileView(View):

    def get(self, request):
        return render(request, 'app_students/profile.html', {})




