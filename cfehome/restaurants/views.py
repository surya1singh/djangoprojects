from django.http import HttpResponse
from django.shortcuts import render

import random

# Create your views here.
def home_function(request):
    return HttpResponse("hello")



def home(request):
    num = random.randint(0, 100000000)
    return render(request, "base.html", {"html_var": True, "num": num})
