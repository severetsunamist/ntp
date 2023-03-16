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
        fields = '__all__'
        labels = {
            'property_type': label('Тип объекта:'),
            'name': label('Название:'),
            'region': label('Регион:'),
            'highway': label('Магистраль:'),
            'location': label('Координаты:'),
            'address': label('Адрес:'),
            'gba': label('Общая площадь:'),
            'gla': label('Арендопригодная площадь:'),
            'built_date': label('Дата ввода в эксплуатацию:'),
            'photo': label('Фото:'),
            'plan': label('План:'),
            'update': label('Дата обновления:')

            # 'owner': label('Собственник:')

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
            'tenant': label('Клиент'),
            'agent': label('Агент'),
            'logo': label('Лого'),
            'industry': label('Направление бизнеса'),
        }