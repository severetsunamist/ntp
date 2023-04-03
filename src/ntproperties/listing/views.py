from django.shortcuts import render
from django.http import HttpResponse
from .models import Property, Block, Company, CompanyCard
from .forms import PropertyForm, CompanyForm, BlockForm, CompanyCardForm


def home_view(request):
    prop = CompanyCard.objects.all()
    # prop = prop.get(id="1")
    column_names = ['id', 'Юр. лицо','ОГРН','ИНН','КПП','Юр. адрес', 'Почтовый адрес', 'Руководитель',
           'Банк', 'Рассчетный счёт','Корреспондентский счёт', 'БИК', 'Телефон','e-mail']

    context = {
        'prop': prop,
        'cn': column_names
    }

    return render(request, "listing.html", context)


def property_create_view(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PropertyForm()

    context = {
        'form': form
    }
    return render(request, 'property_create.html', context)


def block_create_view(request):
    form = BlockForm()
    if request.method == 'POST':
        form = BlockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = BlockForm()
        else:
            print('DATA IS NOT VALID')

    context = {
        'form': form
    }
    return render(request, 'block_create.html', context)


def company_create_view(request):
    form1 = CompanyForm()
    form2 = CompanyCardForm()
    if request.method == 'POST':
        form1 = CompanyForm(request.POST, request.FILES)
        form2 = CompanyCardForm(request.POST)
        if form1.is_valid():
            form1.save()
            form1 = CompanyForm()
        if form2.is_valid():
            form2.save()
            form2 = CompanyCardForm()

    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'company_create.html', context)


# def companycard_create_view(request):
#     form = CompanyCardForm()
#     if request.method == 'POST':
#         form = CompanyCardForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = CompanyCardForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'companycard_create.html', context)

def property_view(request):
    prop = Property.objects.all()
    context = {
        'prop': prop
    }
    return render(request, 'property.html', context)
def property_card_view(request, pk):
    prop = Property.objects.get(id=pk)
    context = {
        'prop': prop
    }
    return render(request, 'property_card.html', context)