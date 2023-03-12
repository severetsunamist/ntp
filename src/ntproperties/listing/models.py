from django.db import models
from django.utils.timezone import now as now
from .models_dropdowns import dropdown

class CompanyCard(models.Model):
    legal_name = models.CharField(max_length=96)
    ogrn = models.CharField(max_length=15)
    inn = models.CharField(max_length=12)
    kpp = models.CharField(max_length=9)
    legal_address = models.CharField(max_length=128)
    post_address = models.CharField(max_length=128)
    ceo = models.CharField(max_length=96)
    bank_name = models.CharField(max_length=64)
    p_account = models.CharField(max_length=20)
    c_account = models.CharField(max_length=20)
    bik = models.CharField(max_length=8)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=48)
    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

class Company(models.Model):
    brand_name = models.CharField(max_length=48, default="NT Properties")
    landlord = models.BooleanField(default=True)
    tenant = models.BooleanField(default=False)
    agent = models.BooleanField(default=False)
    card = models.ForeignKey(CompanyCard, on_delete=models.CASCADE) # FOREIGNKEY
    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Property(models.Model):
    property_type = models.CharField(max_length=dropdown.property_types_max_len, default="Складской комплекс", choices=dropdown.property_types)
    name = models.CharField(max_length=64)
    region = models.CharField(max_length=dropdown.regions_max_len, choices=dropdown.regions)
    highway = models.CharField(max_length=dropdown.highways_max_len, choices=dropdown.highways)
    location = models.CharField(max_length=22)
    address = models.CharField(max_length=256)
    gba = models.PositiveIntegerField()
    gla = models.PositiveIntegerField()
    built_date = models.DateField(default=now)

    # owner = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, default="") # FOREIGNKEY
    update = models.DateField(default=now) # НАСТРОИТЬ ДАТУ ОБНОВЛЕНИЯ
    # img = models.ImageField(upload_to="images/")
    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

class Block(models.Model):
    block_name = models.CharField(max_length=10, default='Блок 1')
    active = models.BooleanField(default=True)

    whs_area = models.PositiveIntegerField()
    office_area = models.PositiveIntegerField()
    mez_area = models.PositiveIntegerField()

    lease_offered = models.BooleanField(default=True)

    lease_whs_price = models.PositiveIntegerField()
    lease_office_price = models.PositiveIntegerField()
    lease_mez_price = models.PositiveIntegerField()

    sale_offered = models.BooleanField(default=False)

    sale_whs_price = models.PositiveIntegerField()
    sale_office_price = models.PositiveIntegerField()
    sale_mez_price = models.PositiveIntegerField()

    _3pl_offered = models.BooleanField(default=False)
    _3pl_price = models.PositiveIntegerField(null=True)

    commercial_comment = models.CharField(max_length=256)

    celling_height = models.PositiveSmallIntegerField()
    column_grid = models.CharField(max_length=7)
    floor_load = models.PositiveSmallIntegerField()
    floor_type = models.CharField(max_length=20)
    docks_amount = models.PositiveSmallIntegerField(null=True)
    gates_amount = models.PositiveSmallIntegerField(null=True)
    fire_system_type = models.CharField(max_length=32)
    el_power = models.CharField(max_length=8)
    heating = models.CharField(max_length=32)

    cross_dock = models.BooleanField(default=False)
    racks = models.BooleanField(default=False)
    cathead = models.BooleanField(default=False)

    tech_comment = models.TextField(max_length=256)

    update = models.DateField(default=now)  # НАСТРОИТЬ ДАТУ ОБНОВЛЕНИЯ

    class Meta:
        verbose_name = 'Площадь'
        verbose_name_plural = 'Площади'


