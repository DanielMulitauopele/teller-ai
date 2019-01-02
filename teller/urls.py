from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomePageView.as_view()),
    path('watson_analysis', views.get_watson_analysis, name='watson_analysis'),
]
