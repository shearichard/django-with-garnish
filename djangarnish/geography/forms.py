from django import forms
from .models import Country, City



class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ["country_iso_code", "population", "area_sq_km"]
        labels = {
            "country_iso_code": "Country",
            "population": "Population",
            "area_sq_km": "Area (sq. km)",
        }
        help_texts = {
            "country_iso_code": "Select the ISO code for the country.",
            "population": "Enter the total population of the country.",
            "area_sq_km": "Enter the total area of the country in square kilometers.",
        }
        widgets = {
            "country_iso_code": forms.Select(attrs={"class": "form-select"}),
            "population": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "area_sq_km": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
        }



class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "country",
            "city_name",
            "mayor_name",
            "date_of_last_mayoral_election",
            "population",
            "area_sq_km",
            "elevation_metres",
            "some_number",
        ]
        labels = {
            "country": "Country",
            "city_name": "City Name",
            "mayor_name": "Mayor's Name",
            "date_of_last_mayoral_election": "Date of Last Mayoral Election",
            "population": "Population",
            "area_sq_km": "Area (sq. km)",
            "elevation_metres": "Elevation (m)",
            "some_number": "Some Number",
        }
        help_texts = {
            "country": "Select the country this city belongs to.",
            "city_name": "Enter the name of the city.",
            "mayor_name": "Enter the current mayor's full name.",
            "date_of_last_mayoral_election": "Provide the date of the last mayoral election (if known).",
            "population": "Enter the city's total population.",
            "area_sq_km": "Enter the area of the city in square kilometers.",
            "elevation_metres": "Enter the city's elevation in meters above sea level.",
            "some_number": "Optional field for any numeric value you wish to record.",
        }
        widgets = {
            "country": forms.Select(attrs={"class": "form-select"}),
            "city_name": forms.TextInput(attrs={"class": "form-control"}),
            "mayor_name": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_last_mayoral_election": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "population": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "area_sq_km": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "elevation_metres": forms.NumberInput(attrs={"class": "form-control"}),
            "some_number": forms.NumberInput(attrs={"class": "form-control"}),
        }

