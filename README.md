
## Summary
Integrating front-end validation for django forms by utilising the constraints defined within django to specify javascript for use on the frontend.

Initially this will be done using the django-parsley package, which in turn relies on the [Parsleyjs](https://parsleyjs.org/) javascript library.

## Parsleyjs Resources

 - [Project Home Page ](https://parsleyjs.org)
 - [Built-in validators](https://parsleyjs.org/doc/index.html#validators)

## Support Tools

### Documentation and Developer Notes

Documentation can be served locally as described [here](djwg-docs/README.md) 

### Virtualenv Management
[pipenv](https://pipenv.pypa.io/en/latest/) is in use as the virtualenv management tool.

### Linting
[flake8](https://flake8.pycqa.org/en/latest/) is used for code quality checking.

Be sure to check the .flake8 file for exclusions from the standard rules.

### Code Formatting
The [black](https://black.readthedocs.io/en/stable/) is installed for automatted code formatting, if that's your thing.

