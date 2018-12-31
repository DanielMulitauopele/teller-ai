from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomePageView.as_view()),
    path('watson_analysis', views.watson_analysis, name='watson_analysis'),
]
