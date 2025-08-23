from django import forms
from .models import Country, City



from django import forms
from .models import Country, City


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"
        widgets = {
            "country_iso_code": forms.Select(attrs={"class": "form-select"}),
            "population": forms.NumberInput(attrs={"class": "form-control"}),
            "area_sq_km": forms.NumberInput(attrs={"class": "form-control"}),
        }
        help_texts = {
            "country_iso_code": "Select the ISO 3166-1 alpha-3 country code.",
            "population": "Enter the population of the country.",
            "area_sq_km": "Enter the land area in square kilometres.",
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"
        widgets = {
            "country": forms.Select(attrs={"class": "form-select"}),
            "city_name": forms.TextInput(attrs={"class": "form-control"}),
            "mayor_name": forms.TextInput(attrs={"class": "form-control"}),
            "date_of_last_mayoral_election": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "population": forms.NumberInput(attrs={"class": "form-control"}),
            "area_sq_km": forms.NumberInput(attrs={"class": "form-control"}),
            "elevation_metres": forms.NumberInput(attrs={"class": "form-control"}),
            "some_number": forms.NumberInput(attrs={"class": "form-control"}),
        }
        help_texts = {
            "country": "Select the country this city belongs to.",
            "city_name": "Enter the name of the city.",
            "mayor_name": "Enter the name of the current mayor.",
            "date_of_last_mayoral_election": "Date of the last mayoral election (if known).",
            "population": "Enter the population of the city.",
            "area_sq_km": "Enter the land area in square kilometres.",
            "elevation_metres": "Enter the elevation in metres above sea level.",
            "some_number": "Optional: provide a number for testing purposes.",
        }




    def clean_city_name(self):
        """Form-level validation example: city name must have at least 2 characters."""
        name = self.cleaned_data.get("city_name")
        if name and len(name.strip()) < 2:
            raise forms.ValidationError("City name must be at least 2 characters long.")
        return name




