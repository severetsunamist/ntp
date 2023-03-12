from django.shortcuts import render
from django.http import HttpResponse
from .models import Property, Block, Company, CompanyCard
from .forms import PropertyForm, CompanyForm, BlockForm, CompanyCardForm


def home_view(request):
    prop = CompanyCard.objects.all().values()

    # prop = prop.get(id="1")

    context = {
        'prop': prop
    }

    return render(request, "listing.html", context)


def property_create_view(request):
    form = PropertyForm(request.POST or None)  # or None)
    if form.is_valid():
        form.save()
        form = PropertyForm()

    context = {
        'form': form
    }
    return render(request, 'property_create.html', context)


def block_create_view(request):
    form = BlockForm(request.POST or None)  # or None)
    if form.is_valid():
        form.save()
        form = BlockForm()

    context = {
        'form': form
    }
    return render(request, 'block_create.html', context)


def company_create_view(request):
    form = CompanyForm(request.POST or None)  # or None)
    if form.is_valid():
        form.save()
        form = CompanyForm()

    context = {
        'form': form
    }
    return render(request, 'company_create.html', context)


def companycard_create_view(request):
    form = CompanyCardForm(request.POST or None)  # or None)
    if form.is_valid():
        form.save()
        form = CompanyCardForm()

    context = {
        'form': form
    }
    return render(request, 'companycard_create.html', context)
