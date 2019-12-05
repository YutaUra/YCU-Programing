from django.urls import path
from .views import TestView, BaseView

urlpatterns = [
    # path('base/', BaseView.as_view()),
    path('', TestView.as_view()),
    path('<path:path>/', TestView.as_view()),
]
