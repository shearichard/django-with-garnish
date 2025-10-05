# Before and After
## Effect of garnishing 

Here is the same input element, in one case without the use of garnishing, and the other with garnishing.

=== "HTML Input (no garnishing)"

    The input element which corresponds to the 'mayor_name' attribute without the use of the @parsleyfy decorator.

    ```html
    <input 
        type="text" 
        name="mayor_name" 
        class="form-control" 
        maxlength="30" 
        minlength="3" 
        required="" 
        aria-describedby="id_mayor_name_helptext" 
        id="id_mayor_name" 
    >
    ```
=== "HTML Input (with garnishing)"

    The input element which corresponds to the 'mayor_name' attribute with the use of the @parsleyfy decorator.

    ```html
    <input 
        type="text" 
        name="mayor_name" 
        class="form-control parsley-error" 
        maxlength="30" minlength="3" 
        data-parsley-required="true" 
        data-parsley-required-message="Please enter the mayor's name." 
        data-parsley-minlength="3" 
        data-parsley-minlength-message="The mayor's name must be at least 3 characters long." 
        data-parsley-maxlength="30" 
        data-parsley-maxlength-message="The mayor's name cannot be longer than 30 characters." 
        required="" 
        aria-describedby="id_mayor_name_helptext" 
        id="id_mayor_name" 
        data-parsley-id="7076"
    >
    ```



## Validation at different levels

To throw light on what triggers parsley.js to introduce the `data-parsley-x` headers seen above here are the validations applied to the `mayor_name` attribute of the `City` model.


=== "Form"

    ```python
    @parsleyfy
    class CityForm(forms.ModelForm):
        mayor_name = forms.CharField(
            min_length=3,
            max_length=30,
            widget=forms.TextInput(attrs={"class": "form-control"}),
            help_text="Enter the name of the current mayor.",
            error_messages={
                "min_length": "The mayor's name must be at least 3 characters long.",
                "max_length": "The mayor's name cannot be longer than 30 characters.",
                "required": "Please enter the mayor's name.",
            },
        )

        class Meta:
            model = City
            fields = "__all__"
            widgets = {
                "country": forms.Select(attrs={"class": "form-select"}),
                "city_name": forms.TextInput(attrs={"class": "form-control"}),
                "date_of_last_mayoral_election": forms.DateInput(
                    attrs={"class": "form-control", "type": "date"}
                ),
                "population": forms.NumberInput(attrs={"class": "form-control"}),
                "area_sq_km": forms.NumberInput(attrs={"class": "form-control"}),
                "elevation_metres": forms.NumberInput(attrs={"class": "form-control"}),
                "some_number": forms.NumberInput(attrs={"class": "form-control"}),
            }
    ```

=== "Model"

    ```python

    class City(models.Model):
        '''
        Represents a City.
        '''
        country = models.ForeignKey(Country, on_delete=models.CASCADE)
        city_name = models.CharField(max_length=255)
        mayor_name = models.CharField(max_length=255)
        date_of_last_mayoral_election = models.DateField(null=True, blank=True)
        population = models.IntegerField()
        area_sq_km = models.IntegerField(null=True, blank=True, validators=[validate_not_divisible_by_seven, validate_even])
        elevation_metres = models.IntegerField(null=True, blank=True)
        some_number = models.IntegerField(blank=True, null=True)

        objects = CityManager()


        class Meta:
            verbose_name_plural = "Cities"


        def clean(self):

            if (self.elevation_metres is not None):
                if (self.elevation_metres > HIGHEST_POINT_ON_LAND):
                    raise ValidationError("Elevation is higher than any point on earth.")

            if (self.elevation_metres is not None):
                if (self.elevation_metres < LOWEST_POINT_ON_LAND):
                    raise ValidationError("Elevation is lower than any point on earth.")

            today = date.today()

            if (self.date_of_last_mayoral_election is not None):
                if (self.date_of_last_mayoral_election > today):
                    raise ValidationError("Date of Last Mayoral Election is after today. If provided, it must be today, or earlier")


        def save(self, *args, **kwargs):
            self.full_clean()
            return super().save(*args, **kwargs)

        def __str__(self):
            return f"{self.city_name} ({self.country.country_iso_code})"
    ```

=== "View"

    _NOTE: In this example no validation is done in the associated views._

    ```python
        
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
    ```


