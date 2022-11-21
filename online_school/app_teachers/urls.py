from django.urls import path, include
from app_teachers.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login")
]
