from django import forms
from .models import Property
from django.utils.translation import gettext_lazy as label

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'name',
            'location',
            'address',
            'type',
            'is_built',
            'gba',
            'gla',
            'owner'
        ]
        labels = {
            'name': label('Название:'),
            'location': label('Координаты:'),
            'address': label('Адрес:'),
            'type': label('Тип объекта:'),
            'is_built': label('Введен в эксплуатацию:'),
            'gba': label('Общая площадь:'),
            'gla': label('Арендопригодная площадь:'),
            'owner': label('Собственник:')
        }
