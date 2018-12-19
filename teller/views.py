from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    response = requests.get('https://guarded-reef-25579.herokuapp.com/api/v1/assets')
    data = response.json()

    return JsonResponse(data, safe=False)
