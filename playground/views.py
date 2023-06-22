from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return render(request,'hello.html', {'name': 'briqz23'})

# Create your views here.
# função que pega request e retorna response
# request handler 