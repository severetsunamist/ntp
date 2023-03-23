from django import forms
from .models import Property, Company, CompanyCard, Block
from django.utils.translation import gettext_lazy as label

class CompanyCardForm(forms.ModelForm):
    class Meta:
        model = CompanyCard
        # fields = [
        #     "legal_name",
        #     'ogrn',
        #     'inn',
        #     'kpp',
        #     'legal_address',
        #     'post_address',
        #     'ceo',
        #     'bank_name',
        #     'p_account',
        #     'c_account',
        #     'bik',
        #     'phone',
        #     'email',
        # ]
        fields = '__all__'
        labels = {
            "legal_name": '',
            'ogrn': '',
            'inn': '',
            'kpp': '',
            'legal_address': '',
            'post_address': '',
            'ceo': '',
            'bank_name': '',
            'p_account': '',
            'c_account': '',
            'bik': '',
            'phone': '',
            'email': '',
        }

        widgets = {
            "legal_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название юр. лица'}),
            'ogrn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ОГРН'}),
            'inn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ИНН'}),
            'kpp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'КПП'}),
            'legal_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Юридический адрес'}),
            'post_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Почтовый адрес'}),
            'ceo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Руководитель'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Банк'}),
            'p_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Расчётный счёт'}),
            'c_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Корреспондентский счёт'}),
            'bik': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'БИК'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e-mail'}),
        }


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        labels = {
            'property_type': '',
            'name': '',
            'region': '',
            'highway': '',
            'location': '',
            'address': '',
            'gba': '',
            'gla': '',
            'built_date': '',
            'photo': '',
            'plan': '',
            'update': '',
            # 'owner': label('Собственник:')
        }
        widgets = {
            'property_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип объекта'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Регион'}),
            'highway': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Шоссе'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Координаты'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес'}),
            'gba': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Общая площадь'}),
            'gla': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Арендопригодная площадь'}),
            'built_date': forms.DateInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Фото'}),
            'plan': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'План'}),
            'update': forms.DateInput(attrs={'class': 'form-control'}),
        }

class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'
        labels = {
            "block_name": label('Название блока'),
            'active': label('На рынке'),

            'whs_area': label('Площадь склада'),
            'office_area': label('Площадь офиса'),
            'mez_area': label('Площадь мезонина'),

            'lease_offered': label('Предлагается в аренду'),

            'lease_whs_price': label('Цена аренды склада'),
            'lease_office_price': label('Цена аренды офиса'),
            'lease_mez_price': label('Цена аренды мезонина'),

            'sale_offered': label('Продаётся'),

            'sale_whs_price': label('Цена за 1 кв. м склада'),
            'sale_office_price': label('Цена за 1 кв. м офиса'),
            'sale_mez_price': label('Цена за 1 кв. м мезонина'),

            '_3pl_offered': label('Предлагаются 3PL услуги'),
            '_3pl_price': label('Цена за 1 пм/сут'),

            'commercial_comment': label('Коммерческие комментарии'),

            'celling_height': label('Высота потолка'),
            'column_grid': label('Сетка колонн'),
            'floor_type': label('Тип полов'),
            'floor_load': label('Макс. нагрузка (т/кв. м)'),
            'docks_amount': label('Кол-во доков'),
            'gates_amount': label('Кол-во ворот'),
            'fire_system_type ': label('Система пожаротушения'),
            'el_power': label('Эл. мощности'),
            'heating': label('Отопление'),

            'cross_dock': label('Кросс-док'),
            'racks': label('Стеллажи'),
            'cathead': label('Кран-балка'),

            'tech_comment': label('Технические комментарии'),

            'photo': label('Фото'),
            'plan': label('План'),

            'update': label('Дата обновления'),

        }
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            "brand_name": label('Название бренда'),
            'landlord': label('Собственник'),
            'client': label('Клиент'),
            'agent': label('Агент'),
            'logist': label('Логистический оператор'),
            'logo': label('Лого'),
            'industry': label('Направление бизнеса'),
        }