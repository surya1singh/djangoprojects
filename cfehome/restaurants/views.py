from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
import random

from .forms import RestaurantCreateForm
from .models import RestaurantLocation

# Create your views here.
def home_function(request):
    return HttpResponse("hello")


def home_base(request):
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
    return render(request, "base_template.html", context)


def about(request):
    context = {
    }
    return render(request, "about.html", context)

class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 100000000),
            random.randint(0, 100000000),
            random.randint(0, 100000000)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 100000000)
        context = {
            "num": num,
            "some_list": some_list
        }
        return context

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()


def restaurant_createview_wrong_way(request):
    # if request.method == "GET":
    #     print("get data")
    if request.method == "POST":
        title = request.POST.get("title") #request.POST["title"]
        location = request.POST.get("location")
        category = request.POST.get("category")
        obj = RestaurantLocation.objects.create(
                name = title,
                location= location,
                category = category

            )
        return HttpResponseRedirect("/restaurants/")
    template_name = 'restaurants/form_wrong_way.html'
    context = {}
    return render(request, template_name, context)

def restaurant_createview(request):
    form = RestaurantCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        obj = RestaurantLocation.objects.create(
                name = form.cleaned_data.get('name'),
                location= form.cleaned_data.get('location'),
                category = form.cleaned_data.get('category')

            )
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)
