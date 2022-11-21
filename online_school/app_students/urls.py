from django.urls import path
from app_students.views import LoginView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile")
]