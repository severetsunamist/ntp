from django.shortcuts import render
from django.http import HttpResponse
from .models import Property
from .forms import PropertyForm

def home_view(request):
    return render(request, "home_navbar.html", {})

def property_create_view(request):
    form = PropertyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PropertyForm()

    context = {
        'form': form
    }
    return render(request, 'property_create.html', context)