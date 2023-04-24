from django import forms
from .models import Property, Company, CompanyCard, Block
from django.utils.translation import gettext_lazy as label
from bootstrap_datepicker_plus.widgets import DatePickerInput

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
            'kad_distance': '',
            'location_latitude': '',
            'location_longitude': '',
            'address': '',
            # 'gba': '',
            'gla': '',
            'built_date': '',
            'photo': 'Фото',
            'plan': 'Генеральный план',
            'update': '',
            # 'owner': label('Собственник:')
        }
        widgets = {
            'property_type': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            'region': forms.Select(attrs={'class': 'form-select'}),
            'highway': forms.Select(attrs={'class': 'form-select'}),
            'kad_distance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '100'}),
            'location_latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'например: 55.750865'}),
            'location_longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'например: 37.618752'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123298, Москва, ул. Складочная, 1'}),
            # 'gba': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Общая площадь, кв. м'}),
            'gla': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '10000'}),
            'built_date': DatePickerInput(attrs={'style': 'border-radius: 0px;', 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'style': 'display: none;', 'class': 'form-control'}),
            'plan': forms.FileInput(attrs={'style': 'display: none;', 'class': 'form-control'}),
            'update': DatePickerInput(attrs={'style': 'border-radius: 0px;', 'class': 'form-control'}),
        }

class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'
        labels = {
            "block_name": '',
            'active': '',

            'total_area': '',
            'whs_area': '',
            'office_area': '',
            'mez_area': '',

            'lease_offered': '',
            'lease_avg_price': '',
            'lease_whs_price': '',
            'lease_office_price': '',
            'lease_mez_price': '',
            'lease_total_price': '',
            'opex': '',
            'opex_included': '',
            'lease_vat_included': '',


            'sale_offered': '',
            'sale_total_price': '',
            'sale_avg_price': '',
            'sale_whs_price': '',
            'sale_office_price': '',
            'sale_mez_price': '',
            'sale_vat_included': '',

            'temp': '',
            'temp_cond_min': '',
            'temp_cond_max': '',
            'log_offered': '',
            'log_price': '',

            'commercial_comment': '',

            'celling_height': '',
            'column_grid': '',
            'floor_type': '',
            'floor_load': '',
            'floor_level': '',
            'docks_amount': '',
            'gates_amount': '',
            'fire_system_type': '',
            'el_power': '',
            'heating': '',

            'cross_dock': '',
            'ramp': '',
            'racks': '',
            'cathead': '',

            'tech_comment': '',

            'photo': '',
            'plan': '',

            'update': '',
        }
        widgets = {
            "block_name": forms.TextInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'col-1 btn-check', 'id': 'check_active', 'autocomplete': 'off', 'checked': True}),

            'total_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'whs_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'office_area': forms.NumberInput(attrs={'class': 'form-control'}),
            'mez_area': forms.NumberInput(attrs={'class': 'form-control'}),

            'lease_offered': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_lease_offered', 'autocomplete': 'off','checked': True}),
            'lease_avg_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'lease_total_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'lease_whs_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'lease_office_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'lease_mez_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'opex': forms.NumberInput(attrs={'class': 'form-control'}),
            'opex_included': forms.CheckboxInput(attrs={'class': 'col-1 btn-check', 'id': 'check_opex_included', 'autocomplete': 'off', 'checked': False}),
            'lease_vat_included': forms.CheckboxInput(attrs={'class': 'col-1 btn-check', 'id': 'check_lease_vat_included', 'autocomplete': 'off', 'checked': False}),

            'sale_offered': forms.CheckboxInput(attrs={'class': 'col-1 btn-check', 'id': 'check_sale_offered', 'autocomplete': 'off', 'checked': False}),
            'sale_total_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_avg_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_whs_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_office_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_mez_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_vat_included': forms.CheckboxInput(attrs={'class': 'col-1 btn-check', 'id': 'check_sale_vat_included', 'autocomplete': 'off', 'checked': False}),

            'temp': forms.CheckboxInput(attrs={'class': 'col-1 btn-check', 'id': 'check_temp', 'autocomplete': 'off', 'checked': False}),
            'temp_cond_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'мин'}),
            'temp_cond_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'макс'}),
            'log_offered': forms.CheckboxInput(attrs={'class': 'col-1 btn-check', 'id': 'check_log_offered', 'autocomplete': 'off', 'checked': False}),
            'log_price': forms.NumberInput(attrs={'class': 'form-control'}),

            'commercial_comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Коммерсекие комментарии'}),

            'celling_height': forms.NumberInput(attrs={'class': 'form-control'}),
            'column_grid': forms.TextInput(attrs={'class': 'form-control'}),
            'floor_type': forms.Select(attrs={'class': 'form-select'}),
            'floor_load': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'docks_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'gates_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'fire_system_type': forms.Select(attrs={'class': 'form-select'}),
            'el_power': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '200 кВт'}),
            'heating': forms.Select(attrs={'class': 'form-select'}),

            'cross_dock': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_cross_dock', 'autocomplete': 'off', 'checked': False}),
            'ramp': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_ramp', 'autocomplete': 'off', 'checked': False}),
            'racks': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_racks', 'autocomplete': 'off', 'checked': False}),
            'cathead': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_cathead', 'autocomplete': 'off', 'checked': False}),

            'tech_comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Технические комментарии'}),

            'photo': forms.FileInput(attrs={'style': 'display: none;', 'class': 'form-control'}),
            'plan': forms.FileInput(attrs={'style': 'display: none;', 'class': 'form-control'}),

            'update': DatePickerInput(attrs={'style': 'border-radius: 0px;', 'class': 'form-control'}),
        }
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            "brand_name": '',
            'landlord': 'Собственник',
            'client': 'Клиент',
            'logist': 'Лог. оператор',
            'agent': 'Агент',
            'logo': '',
            'industry': '',
        }
        widgets = {
            "brand_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название компании'}),
            'landlord': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_landlord', 'autocomplete': 'off', 'checked': True}),
            'client': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_client', 'autocomplete': 'off', 'checked': False}),
            'agent': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_agent', 'autocomplete': 'off', 'checked': False}),
            'logist': forms.CheckboxInput(attrs={'class': 'btn-check', 'id': 'check_logist', 'autocomplete': 'off', 'checked': False}),
            'logo': forms.FileInput(attrs={'style': 'display: none;', 'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Сфера деятельности'}),
        }