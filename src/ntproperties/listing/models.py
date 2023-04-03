from django.db import models
from django.utils.timezone import now as now
from .models_dropdowns import dropdown

class CompanyCard(models.Model):
    legal_name = models.CharField(max_length=96, blank=True)
    ogrn = models.CharField(max_length=15, blank=True)
    inn = models.CharField(max_length=12, blank=True)
    kpp = models.CharField(max_length=9, blank=True)
    legal_address = models.CharField(max_length=128, blank=True)
    post_address = models.CharField(max_length=128, blank=True)
    ceo = models.CharField(max_length=96, blank=True)
    bank_name = models.CharField(max_length=64, blank=True)
    p_account = models.CharField(max_length=20, blank=True)
    c_account = models.CharField(max_length=20, blank=True)
    bik = models.CharField(max_length=8, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=48, blank=True)
    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

class Company(models.Model):
    brand_name = models.CharField(max_length=48)
    landlord = models.BooleanField(default=True)
    client = models.BooleanField(default=False)
    agent = models.BooleanField(default=False)
    logist = models.BooleanField(default=False)
    logo = models.ImageField(null=True, blank=True, upload_to="company/logo")
    industry = models.CharField(max_length=64, blank=True)

    # card = models.ForeignKey(CompanyCard, on_delete=models.CASCADE, blank=True) # FOREIGNKEY
    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Property(models.Model):
    property_type = models.CharField(max_length=dropdown.property_types_max_len,  choices=dropdown.property_types, default="Складской комплекс")
    name = models.CharField(max_length=64, blank=False)
    gla = models.PositiveIntegerField(blank=False)
    # gba = models.PositiveIntegerField(blank=True)
    region = models.CharField(max_length=dropdown.regions_max_len, choices=dropdown.regions, default="Москва", blank=False)
    highway = models.CharField(max_length=dropdown.highways_max_len, choices=dropdown.highways, default="в черте МКАД")
    kad_distance = models.PositiveSmallIntegerField(default=None, null=True, blank=True)
    location_latitude = models.CharField(max_length=10, null=True, blank=False) # широта
    location_longitude = models.CharField(max_length=10, null=True, blank=False) # долгота
    address = models.CharField(max_length=256, blank=True)
    built_date = models.DateField(default=None, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to="property/photo")
    plan = models.ImageField(null=True, blank=True, upload_to="property/plan")

    # owner = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, default="") # FOREIGNKEY
    update = models.DateField(default=now) # НАСТРОИТЬ ДАТУ ОБНОВЛЕНИЯ
    # img = models.ImageField(upload_to="images/")
    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

class Block(models.Model):
    block_name = models.CharField(max_length=10, default='Блок 1')
    active = models.BooleanField(default=True)

    total_area = models.PositiveIntegerField(blank=False)
    whs_area = models.PositiveIntegerField(blank=False)
    office_area = models.PositiveIntegerField(blank=False)
    mez_area = models.PositiveIntegerField(blank=False)

    lease_offered = models.BooleanField(default=True)
    lease_avg_price = models.PositiveIntegerField(null=True, blank=True)
    lease_whs_price = models.PositiveIntegerField(null=True, blank=True)
    lease_office_price = models.PositiveIntegerField(null=True, blank=True)
    lease_mez_price = models.PositiveIntegerField(null=True, blank=True)
    lease_total_price = models.PositiveIntegerField(null=True, blank=True)
    opex = models.PositiveIntegerField(null=True, blank=True)
    opex_included = models.BooleanField(default=False)
    lease_vat_included = models.BooleanField(default=False)

    sale_offered = models.BooleanField(default=False, blank=True)
    sale_total_price = models.PositiveIntegerField(null=True, blank=True)
    sale_avg_price = models.PositiveIntegerField(null=True, blank=True)
    sale_whs_price = models.PositiveIntegerField(null=True, blank=True)
    sale_office_price = models.PositiveIntegerField(null=True, blank=True)
    sale_mez_price = models.PositiveIntegerField(null=True, blank=True)
    sale_vat_included = models.BooleanField(default=False)

    temp = models.BooleanField(default=False)
    temp_cond_min = models.SmallIntegerField(null=True, blank=True)
    temp_cond_max = models.SmallIntegerField(null=True, blank=True)
    log_offered = models.BooleanField(default=False)
    log_price = models.PositiveIntegerField(null=True, blank=True)

    commercial_comment = models.TextField(max_length=256, blank=True)

    celling_height = models.PositiveSmallIntegerField(null=True, blank=True, default=12)
    column_grid = models.CharField(max_length=7, blank=False, default='12 x 24')
    floor_type = models.CharField(max_length=dropdown.floor_types_max_len, choices=dropdown.floor_types, default="Бетон-антипыль")
    floor_load = models.PositiveSmallIntegerField(null=True, blank=True, default=8)
    floor_level = models.FloatField(null=True, blank=True, default=1.2)
    docks_amount = models.PositiveSmallIntegerField(null=True, blank=True, default=10)
    gates_amount = models.PositiveSmallIntegerField(null=True, blank=True, default=1)
    fire_system_type = models.CharField(max_length=dropdown.fire_system_types_max_len, choices=dropdown.fire_system_types, default="Спринклерная система")
    el_power = models.CharField(max_length=8, blank=True, default="200 кВт")
    heating = models.CharField(max_length=dropdown.heating_max_len, choices=dropdown.heating, default="Центральное отопление")

    cross_dock = models.BooleanField(default=False)
    racks = models.BooleanField(default=False)
    ramp = models.BooleanField(default=False)
    cathead = models.BooleanField(default=False)

    tech_comment = models.TextField(max_length=256, blank=True)

    photo = models.ImageField(null=True, blank=True, upload_to="block/photo")
    plan = models.ImageField(null=True, blank=True, upload_to='block/plan')

    update = models.DateField(default=now)  # НАСТРОИТЬ ДАТУ ОБНОВЛЕНИЯ

    class Meta:
        verbose_name = 'Площадь'
        verbose_name_plural = 'Площади'


