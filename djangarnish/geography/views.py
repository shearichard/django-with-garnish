from django.shortcuts import render, redirect, get_object_or_404
from .forms import CountryForm, CityForm
from .models import Country, City

# ------------------------------
# COUNTRY VIEWS
# ------------------------------

def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('geography:country_list')
    else:
        form = CountryForm()
    return render(request, 'geography/country_form.html', {'form': form})


def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('geography:country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'geography/country_form.html', {'form': form})


def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('geography:country_list')
    return render(request, 'geography/country_confirm_delete.html', {'country': country})


def country_list(request):
    countries = Country.objects.all()
    return render(request, 'geography/country_list.html', {'countries': countries})


# ------------------------------
# CITY VIEWS
# ------------------------------

def city_create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('geography:city_list')
    else:
        form = CityForm()
    return render(request, 'geography/city_form.html', {'form': form})


def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('geography:city_list')
    else:
        form = CityForm(instance=city)
    return render(request, 'geography/city_form.html', {'form': form})


def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('geography:city_list')
    return render(request, 'geography/city_confirm_delete.html', {'city': city})


def city_list(request):
    cities = City.objects.all()
    return render(request, 'geography/city_list.html', {'cities': cities})

