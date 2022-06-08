# Jeonse (전세)
An app to compare different rental options. 

With rising loan interest rate and additional fees it is hard to compare multiple `Jeonse` and `Wolse` options at a glance. 

This website gives you a simple way to compare `Jeonse` and `Wolse` rental options. 

Main idea is to bring all options to a single `Monthly expenses` number.

`Monthly expenses` calculated by summing up the `Wolse rent`, `Management fees`, and `Jeonse monthly loan payment amount`.

Monthly loan payment amount is calculated from the `Jeonse` deposit amount only. So, this the only difference between `Jeonse` and `Wolse` deposits in this app. As it is assumed that you will get the loan for the `Jeonse` where as for `Wolse` you are using your own money.

Monthly loan payment amount is calculated by the formula: `Jeonse` deposit amount * `Jeonse` loan interest rate / 12.

If you find yourself not comprehending what the hell I am talking about, please not that it is about housing rental options in South Korea. More info is https://en.wikipedia.org/wiki/Jeonse.
## TODO
* CRUD a listing
* Display numbers nicer
* Create listing form nicer

# DONE
* Add Accounts
* Users listings
* Create a user

## Changes
1. Docker Compose dev and prod setup
1. Templates 
1. Bootstrap 5
1. Logging
1. Pipenv for environment
1. .env file
1. Static files 


## Install
1. `git clone https://github.com/almazkun/django_template.git`
2. `pipenv install`
3. `pipenv shell`
4. `python manage.py startapp <app_name>`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver`



