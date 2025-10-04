# Before and After
## Example of parsleyifed form input element

### Without @parsleyfy
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
### With @parsleyfy
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
