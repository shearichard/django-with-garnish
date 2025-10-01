
## Summary
Integrating front-end validation for django forms by utilising the constraints defined within django to specify javascript for use on the frontend.

Initially this will be done using the django-parsley package, which in turn relies on the [Parsleyjs](https://parsleyjs.org/) javascript library.

## Parsleyjs Resources

 - [Project Home Page ](https://parsleyjs.org)
 - [Built-in validators](https://parsleyjs.org/doc/index.html#validators)

 
## Virtualenv Management
[pipenv](https://pipenv.pypa.io/en/latest/) is in use as the virtualenv management tool.

## Linting
[flake8](https://flake8.pycqa.org/en/latest/) is used for code quality checking.

Be sure to check the .flake8 file for exclusions from the standard rules.

## Code Formatting
The [black](https://black.readthedocs.io/en/stable/) is installed for automatted code formatting, if that's your thing.

----
## Useful references for extending/understanding
```
# after making the virtualenv directory the current directory

$ rg --files-with-matches equalto .
./lib/python3.10/site-packages/parsley/static/parsley/js/parsley.min.js
./lib/python3.10/site-packages/parsley/static/parsley/js/parsley.js
./lib/python3.10/site-packages/parsley/decorators.py
./lib/python3.10/site-packages/parsley/tests/forms.py
./lib/python3.10/site-packages/parsley/tests/tests.py
```

I think the parsley.js file is probably the most useful in terms of understanding what is possible.


### Example of parsleyifed form input element
#### Without @parsleyfy
```
<input 
    type="text" 
    name="mayor_name" 
    class="form-control" 
    maxlength="30" 
    minlength="3" 
    required="" 
    aria-describedby="id_mayor_name_helptext" 
    id="id_mayor_name" 
    data-parsley-id="6635"
>
```
#### With @parsleyfy
```
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
