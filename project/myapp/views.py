from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Welcome to LPU")

def even_odd(request):
    a=100
    if(a%2 == 0):
        return HttpResponse("Number is even")
    else:
        return HttpResponse("Number is Odd")