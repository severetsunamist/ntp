from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=32, default='Московсая область')

    def __str__(self):
        return f"{self.name}"


class Highway(models.Model):
    name = models.CharField(max_length=32, default='внутри МКАД')

    def __str__(self):
        return f"{self.name}"


class Direction(models.Model):
    name = models.CharField(max_length=13, default='Север')

    def __str__(self):
        return f"{self.name}"


class PropertyType(models.Model):
    type = models.CharField(max_length=48, default='Складской комплекс')

    def __str__(self):
        return f"{self.type}"


class AreaType(models.Model):
    type = models.CharField(max_length=24, default='Склад')

    def __str__(self):
        return f"{self.type}"


class Floortype(models.Model):
    type = models.CharField(max_length=16, default='Бетон-антпыль')

    def __str__(self):
        return f"{self.type}"


class ImgType(models.Model):
    type = models.CharField(max_length=16, default='Фото')

    def __str__(self):
        return f"{self.type}"


# main tables

class CompanyCard(models.Model):
    legalName = models.CharField(max_length=64)
    OGRN = models.CharField(max_length=15)
    INN = models.CharField(max_length=12)
    KPP = models.CharField(max_length=9)
    legalAddress = models.CharField(max_length=128)
    postAddress = models.CharField(max_length=128)
    CEO = models.CharField(max_length=96)
    bankName = models.CharField(max_length=64)
    pAccount = models.CharField(max_length=20)
    cAccount = models.CharField(max_length=20)
    BIK = models.CharField(max_length=8)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=48)


class Company(models.Model):
    brandname = models.CharField(max_length=48, default="NT Properties")
    landlord = models.BooleanField(default=True)
    tenant = models.BooleanField(default=False)
    agent = models.BooleanField(default=False)
    card = models.ForeignKey(CompanyCard, on_delete=models.CASCADE)


class Img(models.Model):
    link = models.ImageField()
    imgType = models.ForeignKey(ImgType, on_delete=models.CASCADE)


class Location(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    highway = models.ForeignKey(Highway, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)


class Property(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    gpa = models.IntegerField()
    gla = models.IntegerField()
    builtDate = models.DateField()
    id_objectType = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    id_ownerCompany = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID:{self.id} {self.name} Общ.площадь: {self.gpa}"


class Vacant(models.Model):
    sale = models.BooleanField(default=False)
    lease = models.BooleanField(default=True)
    operations = models.BooleanField(default=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Premise(models.Model):
    vacant = models.ForeignKey(Vacant, on_delete=models.CASCADE, related_name="vacant")
    type = models.ForeignKey(AreaType, on_delete=models.CASCADE)
    area = models.IntegerField()  # sqm
    price = models.IntegerField()  # per 1sqm OR per 1 sqm/year
    cellingHeight = models.PositiveSmallIntegerField()  # m
    columnGrid = models.CharField(max_length=5)
    floorLoad = models.PositiveSmallIntegerField()  # tonnes/sqm
    floorType = models.ForeignKey(Floortype, on_delete=models.CASCADE)
    racks = models.BooleanField(default=False)

