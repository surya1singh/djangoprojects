from django.http import HttpResponse
from django.shortcuts import render

import random

# Create your views here.
def home_function(request):
    return HttpResponse("hello")



def home(request):
    num = None
    some_list = [
        random.randint(0, 100000000),
        random.randint(0, 100000000),
        random.randint(0, 100000000)
    ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0, 100000000)
    context = {
        "num": num,
        "some_list": some_list
    }
    return render(request, "base.html", context)
