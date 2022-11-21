from django.shortcuts import render
from django.views import View
from app_students.forms import LoginForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'app_teachers/login.html', {'form': form})