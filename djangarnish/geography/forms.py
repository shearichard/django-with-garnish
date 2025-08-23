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

    def clean_city_name(self):
        """Example of custom form-level validation (optional)."""
        name = self.cleaned_data.get("city_name")
        if name and len(name) < 2:
            raise forms.ValidationError("City name must be at least 2 characters long.")
        return name

