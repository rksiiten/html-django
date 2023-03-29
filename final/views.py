from django.shortcuts import (render, get_object_or_404)
from django.http import HttpResponseRedirect
from .models import Person
from .forms import PersonForm


# Create your views here.

def create_view(request):
    # dictionary for initial data with field names as key
    context ={}
    # add the dictionary during initialization
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, 'create_view.html', context)

def list_view(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["dataset"] = Person.objects.all()
    return render(request, "list_view.html", context)

def update_view(request, id):
    # fetch the object related to passed id
    obj = Person.objects.get(id = id)
  
    # pass the object as instance in form
    form = PersonForm(request.POST, instance = obj)
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
  
    return render(request, "update_view.html", {'obj':obj})

def delete_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    #context ={}
  
    # fetch the object related to passed id
    obj = Person.objects.get(id = id)
  
  
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return HttpResponseRedirect("/")
  
    return render(request, "delete_view.html",)

def search_view(request):
    if request.method == "POST":
        searched = request.POST['searched']
        pen = Person.objects.filter(brand__contains=searched)
        return render(request, 'search.html', {'searched':searched, 
                    'pen':pen})
    else:
        return render(request, 'search.html')

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def survey(request):
    return render(request, "survey.html")

def us(request):
    return render(request, "us.html")