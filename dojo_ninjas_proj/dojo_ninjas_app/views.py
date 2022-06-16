from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from dojo_ninjas_app.models import Dojo, Ninja

# Create your views here.


def index(request):
    # list all of the tables content
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()

    }
    return render(request, "forms.html", context)


def addDojo(request):
    if request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        state = request.POST.get("state")
        desc = 0  # not assigned in form:)
        Dojo.objects.create(name=name, city=city, state=state, desc=desc)
        return redirect('/')


def addNinja(request):
     if request.method == "POST":
        dojo_id = request.POST.get("dojo")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        dojo = Dojo.objects.get(id=dojo_id) #to get id 

        dojo.count += 1  # add desc by 1 every time a new ninja assigned
        dojo.save()

        Ninja.objects.create(dojo_id=dojo,first_name=first_name,last_name=last_name)
        return redirect('/')

def deleteDojo(request,id):
    dojo = Dojo.objects.get(id=id)
    dojo.delete()

    return redirect('/')
