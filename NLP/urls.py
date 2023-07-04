from django.urls import path
from . import views

urlpatterns = [
    path('analyze', views.API.as_view()),
]