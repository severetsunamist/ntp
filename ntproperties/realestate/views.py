from os.path import splitext
from django.shortcuts import render, redirect
from .forms import (PropertyForm, BlockForm, CompanyForm, CompanyCardForm, ContactForm, RequestForm, DealForm,
                    AgreementForm, PropertyPhotoForm, BlockPhotoForm)
from .models import Block, Request, Activity, PropertyPhoto, BlockPhoto
from .filters import BlockFilter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.views.generic import CreateView
from django_addanother.views import CreatePopupMixin

@login_required
def dashboard_view(request):
    requests = Request.objects.all()
    activities = Activity.objects.all()

    context = {
        'requests': requests,
        'activities': activities,
    }
    return render(request, 'dashboard.html', context)


@login_required
def listing_view(request):
    my_filter, paginated_objects = _block_search_results(request)
    context = {
        'my_filter': my_filter,
        "paginated_objects": paginated_objects,
        "is_search_view": False
    }
    return render(request, 'listing.html', context)


@login_required
def block_search_view(request):
    my_filter, paginated_objects = _block_search_results(request)
    context = {
        'my_filter': my_filter,
        "paginated_objects": paginated_objects,
        "is_search_view": True
    }
    return render(request, 'search_results.html', context)


@login_required
def _block_search_results(request):
    page = request.GET.get("page")

    # property_type = request.GET.get("property_type")
    # sale_offered = request.GET.get("sale_offered")
    # lease_offered = request.GET.get("lease_offered")

    my_filter = BlockFilter(request.GET, queryset=Block.objects.all())
    paginator = Paginator(my_filter.qs, 20)  # my_filter.qs

    try:
        paginated_objects = paginator.get_page(page)
    except PageNotAnInteger:
        paginated_objects = paginator.page(1)
    except EmptyPage:
        paginated_objects = paginator.page(paginator.num_pages)

    return my_filter.form, paginated_objects


@login_required
def map_view(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def create_property_view(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            new_images = request.FILES.getlist('photo')
            if PropertyPhotoForm(new_images).is_valid():
                for image in new_images:  # IMAGE .JPG .JPEG .PNG VALIDATOR
                    if splitext(image.name)[1] != ".jpg" and splitext(image.name)[1] != ".png" and splitext(image.name)[1] != ".jpeg":
                        return redirect('create_property')
                prop = form.save()
                for image in new_images:
                    if image:
                        pic = PropertyPhoto.objects.create(property_id=prop, photo=image)
                        pic.save()
                return redirect('dashboard') # return redirect('flat', flat.pk)

    context = {
        'form': PropertyForm(),
    }
    return render(request, 'create_property.html', context)


@login_required
def create_block_view(request):
    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            new_images = request.FILES.getlist('photo')
            if BlockPhotoForm(new_images).is_valid():
                for image in new_images:  # IMAGE .JPG .JPEG .PNG VALIDATOR
                    if splitext(image.name)[1].lower() != ".jpg" and splitext(image.name)[1].lower() != ".png" and splitext(image.name)[1].lower() != ".jpeg":
                        return redirect('create_block')
                block = form.save()
                for image in new_images:
                    if image:
                        pic = BlockPhoto.objects.create(block_id=block, photo=image)
                        pic.save()
                return redirect('dashboard') # return redirect('flat', flat.pk)

    context = {
        'form': BlockForm(),
    }
    return render(request, 'create_block.html', context)


@login_required
def create_company_view(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': CompanyForm(),
    }
    return render(request, 'create_company.html', context)


class ComapnyCardView(CreatePopupMixin, CreateView):
    def get(self, request):
        if request.method == 'POST':
            form = CompanyCardForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        context = {
            'form': CompanyCardForm(),
        }
        context['view'] = self
        return render(request, 'create_companycard.html', context)

# @login_required
# def create_companycard_view(request):
#     if request.method == 'POST':
#         form = CompanyCardForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': CompanyCardForm(),
#     }
#     return render(request, 'create_companycard.html', context)


@login_required
def create_contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': ContactForm(),
    }
    return render(request, 'create_contact.html', context)


@login_required
def create_request_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': RequestForm(),
    }
    return render(request, 'create_request.html', context)


@login_required
def create_deal_view(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': DealForm(),
    }
    return render(request, 'create_deal.html', context)


@login_required
def create_agreement_view(request):
    if request.method == 'POST':
        form = AgreementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': AgreementForm(),
    }
    return render(request, 'create_agreement.html', context)


@login_required
def create_several_view(request):
    prop_form = PropertyForm()
    block_form = BlockForm()
    if request.method == "POST":
        prop_form = PropertyForm(request.POST)
        block_form = BlockForm(request.POST)
        if prop_form.is_valid():
            prop = prop_form.save()
            if block_form.is_valid():
                block = block_form.save(commit=False)
                block.parent_property = prop
                block_form.save()
            else:
                print("Form2 is NOT valid")
        else:
            print("Form1 is NOT valid")

    context = {
        'form1': prop_form,
        'form2': block_form,
    }
    return render(request, 'create_several.html', context)


@login_required
def block_view(request, pk):
    block_data = Block.objects.get(id=pk)
    block_data.save()
    images = BlockPhoto.objects.filter(block_id=pk)
    lat = block_data.parent_property.location.partition(", ")[0]
    long = block_data.parent_property.location.partition(", ")[2]
    context = {
        'block_data': block_data,
        'images': images,
        'lat': lat,
        'long': long,
    }
    return render(request, 'block.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        initial_url_requested = redirect(request.POST.get("next"))
        if user is not None:
            login(request, user)
            if request.POST.get("next"):
                return initial_url_requested
            else:
                return redirect('dashboard')
        else:
            messages.error(request, ('Неверный логин или пароль, попробуйте снова...'))
            return initial_url_requested

    else:
        return render(request, 'login.html', {})