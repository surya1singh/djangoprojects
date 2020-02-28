from django.forms import modelformset_factory
from django.shortcuts import render,redirect
from .models import Animals
#from .forms import AnimalsForm



def index(request):
    animals = Animals.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST: #checking if there is a request to add a animal
            title = request.POST["name"] #title
            content = request.POST["description"]
            Animal = Animals(title=title, content=content)
            Animal.save() #saving the animal
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a animal
            checkedlist = request.POST["checkedbox"] #checked animals to be deleted
            for animal_id in checkedlist:
                animal = Animals.objects.get(id=int(animal_id)) #getting animal id
                animal.delete() #deleting animal
    return render(request, "index.html", {"Animals": animals})


def add_animals(request):
#    AnimalFormSet = modelformset_factory(Animals, fields=('title', 'content'))
    if request.method == 'POST':
        formset = AnimalsForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = AnimalsForm()
    return render(request, 'manage_animals.html', {'formset': formset})
