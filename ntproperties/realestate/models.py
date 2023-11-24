# import django.contrib.auth.models
from django.conf import settings
from django.db import models
from .models_dropdowns import *


class Company(models.Model):
    name = models.CharField("Назавание", max_length=30, null=False, blank=False)
    is_client = models.BooleanField('Клиент', default=True)
    is_logist = models.BooleanField('Логист', default=False)
    is_landlord = models.BooleanField('Собственник', default=False)
    is_developer = models.BooleanField('Девелопер', default=False)
    is_pm = models.BooleanField('Управляющая компания', default=False)
    is_broker = models.BooleanField('Брокер', default=False)
    is_subcontractor = models.BooleanField('Подрядчик', default=False)
    website = models.CharField('Сайт', max_length=40, null=True, blank=True)

    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class CompanyCard(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='company_cards', null=True, verbose_name="Компания")
    legal_name = models.CharField("Наименование", max_length=96, null=False, blank=False)
    ogrn = models.CharField("ОГРН", max_length=15, null=False, blank=False)
    inn = models.CharField("ИНН", max_length=12, null=False, blank=False)
    kpp = models.CharField("КПП", max_length=9, null=False, blank=False)
    legal_address = models.CharField("Юридический адрес", max_length=128, null=False, blank=False)
    post_address = models.CharField("Почтовый адрес", max_length=128, null=False, blank=False)
    ceo = models.CharField("Генеральный директор", max_length=96, null=False, blank=False)
    bank_name = models.CharField("Банк", max_length=64, null=False, blank=False)
    p_account = models.CharField("Расчётный счёт", max_length=20, null=False, blank=False)
    c_account = models.CharField("Корреспондентский счёт", max_length=20, null=False, blank=False)
    bik = models.CharField("БИК", max_length=8, null=False, blank=False)
    phone = models.CharField("Телефон", max_length=15, null=False, blank=False)
    email = models.CharField("Электронный адрес", max_length=48, null=False, blank=False)

    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    def __str__(self):
        return str(self.legal_name) + ' ИНН: ' + str(self.inn)


class Contact(models.Model):
    employer = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='contact', null=True, blank=True, verbose_name="Компания")
    name = models.CharField("ФИО", max_length=60, null=False)
    phone_number = models.CharField('Рабочий номер телефона', max_length=12, null=False)
    email = models.CharField('Рабочий e-mail', max_length=40)
    title = models.CharField("Должность", max_length=20, null=False, blank=True)
    additional_info = models.CharField("Дополнительная информция", max_length=256, null=True, blank=True)
    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        if self.employer:
            return str(self.name) + str(self.employer)
        else:
            return str(self.name) + str(self.phone_number)


class Property(models.Model):
    property_type = models.CharField("Тип объекта", choices=industrial_property_types, max_length=34, default=industrial_property_types[0][0])
    name = models.CharField("Название объекта", max_length=64, null=False, blank=False)
    region = models.CharField("Регион", choices=regions, max_length=15, default=regions[0][0])
    highway = models.CharField("Шоссе", choices=highways, max_length=25, default=highways[0][0])
    kad_distance = models.PositiveSmallIntegerField("Расстояние от кольцевой, км", null=True, blank=True)
    location = models.CharField("Координаты", max_length=25, null=False, blank=False)
    total_area = models.PositiveIntegerField("Общая площадь, кв. м", null=False, blank=False)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name="Контакт", related_name='properties')
    owner = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Собственник", related_name='properties', null=True, blank=True)
    is_built = models.BooleanField("Введён в эксплуатацию", default=True)
    built_date = models.DateField("Дата ввода в экусплуатацию", auto_now_add=False, null=True, blank=True)

    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

    def __str__(self):
        return self.name


class Block(models.Model):
    parent_property = models.ForeignKey(Property, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Часть объекта")

    vacant_status = models.CharField("Статус готовности", choices=vacant_statuses, max_length=14, default=vacant_statuses[0][0])
    date_become_vacant = models.DateField("Дата готовности", auto_now_add=False, null=True, blank=True)

    total_area = models.PositiveIntegerField("Общая площадь, кв. м", null=True, blank=True)
    whs_area = models.PositiveIntegerField("Площадь склада, кв. м", null=True, blank=True)
    office_area = models.PositiveIntegerField("Площадь офиса, кв. м", null=True, blank=True)
    mez_area = models.PositiveIntegerField("Площадь мезонина,  кв. м", null=True, blank=True)

    lease_offered = models.BooleanField("Аренда", default=True)

    lease_whs_price = models.PositiveIntegerField("Склад, руб/кв. м/год", null=True, blank=True)
    lease_office_price = models.PositiveIntegerField("Офис, руб/кв. м/год", null=True, blank=True)
    lease_mez_price = models.PositiveIntegerField("Мезонин, руб/кв. м/год", null=True, blank=True)
    lease_avg_price = models.PositiveIntegerField("Средняя ставка аренды, руб/кв. м/год", null=True, blank=True)
    lease_total_price = models.PositiveIntegerField("Полная стоимость аренды, руб/мес", null=True, blank=True)
    opex = models.PositiveIntegerField("ОРЕХ, руб/кв. м/год", null=True, blank=True)
    opex_included = models.BooleanField("ОРЕХ включён", default=False)
    lease_vat_included = models.BooleanField("НДС включён", default=False)

    sale_offered = models.BooleanField("Продажа", default=False)
    sale_total_price = models.PositiveIntegerField("Цена продажи, руб", null=True, blank=True)
    sale_avg_price = models.PositiveIntegerField("Средня цена за кв. м, руб/кв. м", null=True, blank=True)
    sale_whs_price = models.PositiveIntegerField("Склад, руб/кв. м", null=True, blank=True)
    sale_office_price = models.PositiveIntegerField("Офис, руб/кв. м/год", null=True, blank=True)
    sale_mez_price = models.PositiveIntegerField("Мезонин, руб/кв. м", null=True, blank=True)
    sale_vat_included = models.BooleanField("НДС включён", default=False)

    commercial_comment = models.TextField("Коммерческие комментарии", max_length=256, blank=True)

    celling_height = models.PositiveSmallIntegerField("Высота потолков, м", null=False, default=12)
    column_grid = models.CharField("Шаг колонн, м", choices=column_grid, max_length=11, default=column_grid[0][0])
    floor_type = models.CharField("Тип полов", choices=floor_types, max_length=19, default=floor_types[0][0])
    floor_load = models.PositiveSmallIntegerField("Нагрузка на полы, т/кв. м", null=True, blank=True, default=8)
    docks_amount = models.PositiveSmallIntegerField("Кол-во доков", null=True, blank=True, default=10)
    gates_amount = models.PositiveSmallIntegerField("Кол-во ворот", null=True, blank=True, default=0)
    fire_alarm = models.BooleanField("Пожарная сигнализация", default=True)
    fire_system_type = models.CharField("Противопожарная система", max_length=12, choices=fire_system_types, default=fire_system_types[0][0])
    heating = models.CharField("Отопление", max_length=21, choices=heating, default=heating[0][0])
    el_power = models.IntegerField("Эл. мощности, кВт", null=True, blank=True)
    cross_dock = models.BooleanField("Кросс-док", default=False)
    ramp = models.BooleanField("Рампа", default=False)
    racks = models.BooleanField("Установлены стеллажи", default=False)
    cathead = models.BooleanField("Кран-балка", default=False)

    ventilation = models.BooleanField("Доп. вентиляция", default=False)
    temp = models.BooleanField("Температурные режим", default=False)
    temp_cond_max = models.SmallIntegerField("Макс. температура, ℃", null=True, blank=True)
    temp_cond_min = models.SmallIntegerField("Мин. температура, ℃", null=True, blank=True)

    tech_comment = models.TextField("Технические комментарии", max_length=256, null=True, blank=True)

    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'

    def __str__(self):
        if self.total_area:
            return str(self.total_area) + ' кв. м в ' + str(self.parent_property)
        return str(int(self.whs_area) + int(self.office_area) + int(self.mez_area)) + ' кв. м в ' + str(self.parent_property)


class Request(models.Model):
    broker = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL, verbose_name="Ответственный брокер")
    client = models.ForeignKey(Contact, null=False, on_delete=models.PROTECT, verbose_name="Контакт клиента")
    lease = models.BooleanField("Аренда", default=False)
    buy = models.BooleanField("Покупка", default=False)
    bts = models.BooleanField("Build-to-suit", default=False)
    whs_area = models.PositiveIntegerField("Склад, кв. м", null=True,  blank=True)
    office_area = models.PositiveIntegerField("Офис, кв. м", null=True, blank=True)
    mez_area = models.PositiveIntegerField("Мезонин, кв. м", null=True, blank=True)
    comment = models.TextField("Дополнительная информация", max_length=512, null=True, blank=True)
    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        total_area_min = sum(filter(None, [self.whs_area, self.office_area, self.mez_area]))
        goal = "Аренда/Покупка" if self.lease and self.buy else "Аренда" if self.lease else "Покупка" if self.buy else ""
        bts = "BTS" if self.bts else ""
        return f"{self.client}, {goal} {bts}, {total_area_min} кв. м"


class Agreement(models.Model):
    contract_type = models.CharField("Тип договора", max_length=33, choices=contract_types, default=contract_types[0][0])
    party_1 = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False, verbose_name="Сторона 1", related_name="agreemant_p1")
    party_2 = models.ForeignKey(Company, on_delete=models.PROTECT, null=False, blank=False, verbose_name="Сторона 2", related_name="agreemant_p2")
    commission = models.FloatField("Комиссия, %", null=True, blank=True)
    under_negotiation = models.BooleanField("На согласовании", null=True, blank=True)
    signed = models.FileField("Финальная версия", null=True, blank=True)
    date = models.DateField("Дата заключения договора", null=True, blank=True)

    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        return str(self.contract_type) + " " + str(self.party_1) + " " + str(self.party_1)  + " от " + str(self.date)


class Deal(models.Model):
    buyer = models.ForeignKey(Company, null=True, on_delete=models.PROTECT, verbose_name="Покупатель / Арендатор", related_name="deal_buyer")
    seller = models.ForeignKey(Company, null=True, on_delete=models.PROTECT, verbose_name="Продавец / Арендодатель", related_name="deal_seller")

    sale = models.BooleanField("Покупка", default=False)
    lease = models.BooleanField("Аренда", default=False)

    total_area = models.PositiveIntegerField("Общая площадь, кв. м", null=True, blank=True)
    whs_area = models.PositiveIntegerField("Площадь склада, кв. м", null=True, blank=True)
    office_area = models.PositiveIntegerField("Площадь офиса, кв. м", null=True, blank=True)
    mez_area = models.PositiveIntegerField("Площадь мезонина,  кв. м", null=True, blank=True)

    is_ours = models.BooleanField("Наша сделка", default=False)
    our_broker = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Брокер NT Properties")

    competitor_company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Компания конкурент")
    competitor_broker = models.ForeignKey(Contact, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Брокер конкурент")

    deal_date = models.DateField("Дата заключения сделки", null=True, blank=True)
    contract_length = models.SmallIntegerField("Срок договора, лет", null=True, blank=True)

    lease_total_price = models.FloatField("Полная цена договора аренды", null=True, blank=True)
    lease_whs_price_sqm = models.FloatField("Ставка аренды склада, руб/кв. м/год", null=True, blank=True)
    lease_office_price_sqm = models.FloatField("Ставка аренды офиса, руб/кв. м/год", null=True, blank=True)
    lease_mez_price_sqm = models.FloatField("Ставка аренды мезонина, руб/кв. м/год", null=True, blank=True)
    lease_opex_sqm = models.FloatField("ОРЕХ, руб/кв. м/год", null=True, blank=True)
    lease_opex_included = models.BooleanField("ОРЕХ включён", default=False)
    lease_vat_included = models.BooleanField("НДС включён", default=False)

    sale_total_price = models.FloatField("Полная цена договора аренды", null=True, blank=True)
    sale_whs_price_sqm = models.FloatField("Ставка аренды склада, руб/кв. м/год", null=True, blank=True)
    sale_office_price_sqm = models.FloatField("Ставка аренды офиса, руб/кв. м/год", null=True, blank=True)
    sale_mez_price_sqm = models.FloatField("Ставка аренды мезонина, руб/кв. м/год", null=True, blank=True)
    sale_vat_included = models.BooleanField("НДС включён", default=False)

    agreement = models.ForeignKey(Agreement, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Договор")

    db_update_date = models.DateField("Дата обновления", auto_now_add=True)

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self):
        if self.total_area:
            return str(self.buyer) + ' - ' + str(self.seller) + " " + str(self.total_area) + ' кв. м ' + str(self.deal_date)
        return str(self.buyer) + ' - ' + str(self.seller) + " " + str(int(self.whs_area) + int(self.office_area) + int(self.mez_area)) + ' кв. м ' + str(self.deal_date)

class Activity(models.Model):
    broker = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.PROTECT, verbose_name="Брокер")
    contact = models.ForeignKey(Contact, null=False, blank=False, on_delete=models.PROTECT, verbose_name="Контакт")
    comment = models.TextField("Комментарий", null=False, blank=False, max_length=256)
    date = models.DateTimeField("Дата активности", auto_now_add=True)
    activity_type = models.CharField("Вид активности", max_length=11, choices=activity_types, default=activity_types[0][0])
    activity_subject = models.CharField("Предмет активности", max_length=7, choices=activity_subjects, default=activity_subjects[0][0])

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'

    def __str__(self):
        return f"[ {self.date.strftime('%d.%m.%Y')} {self.activity_type} {self.activity_subject} ] [ {self.broker} -> {self.contact} ]"


class PropertyPhoto(models.Model):
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_photos')
    photo = models.ImageField('Фото объекта', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото объекта'
        verbose_name_plural = 'Фото объекта'

class BlockPhoto(models.Model):
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='block_photos')
    photo = models.ImageField('Фото блока', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото блоков'
        verbose_name_plural = 'Фото блоков'


