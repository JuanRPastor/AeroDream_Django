from django.db import models

# Create your models here.


class Airplane(models.Model):
    model = models.CharField(max_length=50)
    year = models.DateField()
    company = models.CharField(max_length=30)
    passengerCapaCity = models.PositiveIntegerField()
    fuelCapacity = models.IntegerField()
    kmInDrive = models.FloatField()

    def __str__(self):
        return self.model


# ---------------------------------------------------------------------------------------------------------------


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------------------------------------------


class TimeZone(models.Model):
    name = models.CharField(max_length=50, unique=True, default="000")

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------------------------------------------


class City(models.Model):
    name = models.CharField(max_length=20, unique=True)
    Country = models.ForeignKey(Country, to_field="name", on_delete=models.CASCADE)
    time_zone = models.ForeignKey(
        TimeZone, to_field="name", on_delete=models.CASCADE, default="000"
    )

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------------------------------------------


class Airoport(models.Model):
    name = models.CharField(null=False, max_length=30)
    iata_code = models.CharField(max_length=3, unique=True, default="Unknow")
    city = models.ForeignKey(City, on_delete=models.CASCADE, to_field="name")
    clasification = models.CharField(
        max_length=50,
        choices=[
            ("Internacional", "Internacional"),
            ("Nacional", "Nacional"),
        ],
        default="Nacional",
    )
    contact = models.CharField
    email = models.CharField

    def __str__(self):
        return self.name


# ---------------------------------------------------------------------------------------------------------------


class Airlain(models.Model):
    name = models.CharField(max_length=40)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT, to_field="name")
    airoport = models.ManyToManyField(Airoport, related_name="Airoport")

    def __str__(self):
        return self.name


# # ---------------------------------------------------------------------------------------------------------------


# class Destination(models.Model):
#     City = models.ForeignKey(City, on_delete=models.CASCADE)
#     Country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     Airoport = models.ForeignKey(Airoport, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.place


# # ---------------------------------------------------------------------------------------------------------------


class Route(models.Model):
    origen = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="origen_Routss"
    )
    destination = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="destination_Route"
    )
    kmTotals = models.FloatField()
    price = models.FloatField(null=False)


# ---------------------------------------------------------------------------------------------------------------
