from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('survey_info', views.survey),
    path('result', views.success)
]