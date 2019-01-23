import requests

from django.shortcuts import render
from django.views.generic import TemplateView


class WelcomePageView(TemplateView):
    def get(self, request):
        return render(request, 'welcome.html')
