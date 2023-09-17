from django.contrib import admin
from .models import (
    Airplane,
    Country,
    Route,
    Airoport,
    TimeZone,
    Airlain,
    City,
)

# Register your models here.

admin.site.register(Airplane)
admin.site.register(Country)
admin.site.register(TimeZone)
admin.site.register(Airlain)
admin.site.register(City)
admin.site.register(Airoport)
admin.site.register(Route)
