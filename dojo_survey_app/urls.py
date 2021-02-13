from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('survey_data', views.survey),
    path('result', views.success)
]