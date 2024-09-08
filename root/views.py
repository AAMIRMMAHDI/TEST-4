from django.shortcuts import render
from .models import Services , Events
from course.models import Catergory

def home(request):
    #services = Services.objects.all()
    services = Services.objects.filter(status=True)
    catergory = Catergory.objects.all()
    return render(request,"root/index.html",context={"services":services})

def contact(request):
    return render(request,"root/contact.html")

def about(request):
    return render(request,"root/about.html")

def events(request):
    events = Events.objects.filter(status = True)
    context = {
        'events':events
    }
    return render(request,"root/events.html",context=context)
