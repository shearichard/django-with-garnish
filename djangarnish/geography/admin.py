from django.contrib import admin

from .models import Country, City 

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_iso_code', 'population', 'area_sq_km')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('country__country_iso_code', 'mayor_name', 'date_of_last_mayoral_election', 'area_sq_km', 'elevation_metres')

