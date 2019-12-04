from django.contrib import admin
from django.urls import path
from core import views as v

urlpatterns = [
    path('', v.BaseView.as_view()),
    path('setting/', v.SettingChangeView.as_view()),
]
