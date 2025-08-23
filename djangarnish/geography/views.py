from django.shortcuts import render, redirect
from .forms import CountryForm, CityForm

# ------------------------------
# View for creating a Country
# ------------------------------
def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # adjust this to your home page or country list
    else:
        form = CountryForm()

    return render(request, 'geography/country_form.html', {'form': form})


# ------------------------------
# View for creating a City
# ------------------------------
def city_create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # adjust this to your home page or city list
    else:
        form = CityForm()

    return render(request, 'geography/city_form.html', {'form': form})

