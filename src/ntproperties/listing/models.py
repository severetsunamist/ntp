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
    brand_name = models.CharField(max_length=48, default="NT Properties")
    landlord = models.BooleanField(default=True)
    tenant = models.BooleanField(default=False)
    agent = models.BooleanField(default=False)
    logo = models.ImageField(null=True, blank=True)
    industry = models.CharField(max_length=64, blank=True)

    # card = models.ForeignKey(CompanyCard, on_delete=models.CASCADE, blank=True) # FOREIGNKEY
    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Property(models.Model):
    property_type = models.CharField(max_length=dropdown.property_types_max_len,  choices=dropdown.property_types, default="Складской комплекс")
    name = models.CharField(max_length=64)
    region = models.CharField(max_length=dropdown.regions_max_len, choices=dropdown.regions, default="Москва")
    highway = models.CharField(max_length=dropdown.highways_max_len, choices=dropdown.highways, default="в черте МКАД")
    location = models.CharField(max_length=22, blank=True) # make map location picker
    address = models.CharField(max_length=256, blank=True)
    gba = models.PositiveIntegerField(blank=True)
    gla = models.PositiveIntegerField(blank=True)
    built_date = models.DateField(default=now)
    photo = models.ImageField(null=True, blank=True)
    plan = models.ImageField(null=True, blank=True)

    # owner = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, default="") # FOREIGNKEY
    update = models.DateField(default=now) # НАСТРОИТЬ ДАТУ ОБНОВЛЕНИЯ
    # img = models.ImageField(upload_to="images/")
    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

class Block(models.Model):
    block_name = models.CharField(max_length=10, default='Блок 1')
    active = models.BooleanField(default=True)

    whs_area = models.PositiveIntegerField(blank=True)
    office_area = models.PositiveIntegerField(blank=True)
    mez_area = models.PositiveIntegerField(blank=True)

    lease_offered = models.BooleanField(default=True, blank=True)

    lease_whs_price = models.PositiveIntegerField(default=7000)
    lease_office_price = models.PositiveIntegerField(default=15000)
    lease_mez_price = models.PositiveIntegerField(default=6000)

    sale_offered = models.BooleanField(default=False, blank=True)

    sale_whs_price = models.PositiveIntegerField(default=40000)
    sale_office_price = models.PositiveIntegerField(default=48000)
    sale_mez_price = models.PositiveIntegerField(default=35000)

    _3pl_offered = models.BooleanField(default=False, blank=True)
    _3pl_price = models.PositiveIntegerField(null=True, blank=True)

    commercial_comment = models.TextField(max_length=256, blank=True)

    celling_height = models.PositiveSmallIntegerField(default=12)
    column_grid = models.CharField(max_length=7, default='12 x 24')
    floor_type = models.CharField(max_length=20, blank=True)
    floor_load = models.PositiveSmallIntegerField(default=8)
    docks_amount = models.PositiveSmallIntegerField(default=10)
    gates_amount = models.PositiveSmallIntegerField(default=1)
    fire_system_type = models.CharField(max_length=dropdown.fire_system_types_max_len, choices=dropdown.fire_system_types, default="Спринклерная система пожаротушения")
    el_power = models.CharField(max_length=8, default="200 кВт")
    heating = models.CharField(max_length=dropdown.heating_max_len, choices=dropdown.heating, default="Центральное отопление")

    cross_dock = models.BooleanField(default=False)
    racks = models.BooleanField(default=False)
    cathead = models.BooleanField(default=False)

    tech_comment = models.TextField(max_length=256, blank=True)

    photo = models.ImageField(null=True, blank=True)
    plan = models.ImageField(null=True, blank=True)

    update = models.DateField(default=now)  # НАСТРОИТЬ ДАТУ ОБНОВЛЕНИЯ

    class Meta:
        verbose_name = 'Площадь'
        verbose_name_plural = 'Площади'


