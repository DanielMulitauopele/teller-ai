from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    query = 'bitcoin'
    url = f'https://api.twitter.com/1.1/search/tweets.json?q={query}&lang=en'
    headers = {'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAISA9AAAAAAAW5acT9%2BlGGBQc%2BEslGwUlYjEz8o%3Dog6Fe533FdcoaLlcikecwqRoQMrt9kVIDrbeB5fxktdv0UpCvC'}
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data, safe=False)
