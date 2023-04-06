from django.contrib import admin
from django.urls import path, include
from account.views import RegisterView, LoginView

urlpatterns = [
    path('signup/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]