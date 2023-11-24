from .models import Property, Contact, Company, CompanyCard, Block, Request, Agreement, Deal, BlockPhoto, PropertyPhoto
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

from django.urls import reverse_lazy
from django_addanother.contrib.select2 import Select2AddAnother


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

        # widgets = {
        #     'built_date': DatePickerInput(),
        # }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyCardForm(forms.ModelForm):
    class Meta:
        model = CompanyCard
        fields = '__all__'
        widgets = {
            'company': Select2AddAnother(reverse_lazy('create_company')),
        }


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = '__all__'


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = '__all__'


class PropertyPhotoForm(forms.ModelForm):
    class Meta:
        model = PropertyPhoto
        fields = ['photo']


class BlockPhotoForm(forms.ModelForm):
    class Meta:
        model = BlockPhoto
        fields = ['photo']