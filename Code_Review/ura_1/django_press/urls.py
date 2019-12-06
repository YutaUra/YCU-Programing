from django.urls import path
from django_press.views import TestView

urlpatterns = [
    path('', TestView.as_view()),
]
