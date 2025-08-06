from django.http import HttpResponse,HttpResponseNotFound
import requests
from django.http import JsonResponse


def hello(request):
    return HttpResponse("Hello, Welcome to LPU")

def even_odd(request):
    a=100
    if(a%2 == 0):
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is Odd")

def siddu(request):
    return HttpResponse("Helloo Sidduuu")

def get_api_data(request,id):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}'
    response = requests.get(url)

    if response.status_code== 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Data not found"},status =404)

def json_view(request):
    data = {"name":"Siddu","course":"Django"}
    return JsonResponse(data)

def jsonsecond(request,data):
    d = {
        "name":"Sidhartha",
        "course":["Django","Python","Java","Fullstack"],
        "city":"Dharmavaram"
    }

    if data in d:
        return JsonResponse({data: d[data]})
    else:
        return HttpResponseNotFound(f"Key '{data}' not found.")