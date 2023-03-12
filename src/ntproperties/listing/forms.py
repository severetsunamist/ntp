from django import forms
from .models import Property, Company, CompanyCard, Block
from django.utils.translation import gettext_lazy as label

class CompanyCardForm(forms.ModelForm):
    class Meta:
        model = CompanyCard
        fields = [
            "legal_name",
            'ogrn',
            'inn',
            'kpp',
            'legal_address',
            'post_address',
            'ceo',
            'bank_name',
            'p_account',
            'c_account',
            'bik',
            'phone',
            'email',
        ]
        labels = {
            "legal_name": label('Название'),
            'ogrn': label('ОГРН'),
            'inn': label('ИНН'),
            'kpp': label('КПП'),
            'legal_address': label('Юридический адрес'),
            'post_address': label('Почтовый адрес'),
            'ceo': label('Руководитель'),
            'bank_name': label('Банк'),
            'p_account': label('Рассчётный счёт'),
            'c_account': label('Корреспондентский счёт'),
            'bik': label('БИК'),
            'phone': label('Телефон'),
            'email': label('Электронный адрес'),
        }


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'property_type',
            'name',
            'location',
            'address',
            'built_date',
            'gba',
            'gla',
            # 'owner'
            # 'img',
        ]
        labels = {
            'property_type': label('Тип объекта:'),
            'name': label('Название:'),
            'location': label('Координаты:'),
            'address': label('Адрес:'),
            # 'object_type': label('Тип объекта:'),
            'built_date': label('Дата ввода в эксплуатацию:'),
            'gba': label('Общая площадь:'),
            'gla': label('Арендопригодная площадь:'),
            # 'img': label('Фото:'),
            # 'owner': label('Собственник:')
            'property_type': label('Тип объекта:'),
        }

class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = [
            "block_name",
            'active',
            'whs_area',
            'office_area',
            'mez_area',
        ]
        labels = {
            "block_name": label('Название блока'),
            'active': label('На рынке'),
            'whs_area': label('Площадь склада'),
            'office_area': label('Площадь офиса'),
            'mez_area': label('Площадь мезонина'),
        }
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "brand_name",
            'landlord',
            'tenant',
            'agent',
        ]
        labels = {
            "brand_name": label('Название бренда'),
            'landlord': label('Собственник'),
            'tenant': label('Клиент'),
            'agent': label('Агент'),
        }