# Jeonse (전세)

Demo: https://jeonse.akun.dev

An app to compare different rental options. 

With rising loan interest rate and additional fees it is hard to compare multiple `Jeonse` and `Wolse` options at a glance. 

This website gives you a simple way to compare `Jeonse` and `Wolse` rental options. 

Main idea is to bring all options to a single `Monthly expenses` number.

`Monthly expenses` calculated by summing up the `Wolse rent`, `Management fees`, and `Jeonse monthly loan payment amount`.

Monthly loan payment amount is calculated from the `Jeonse` deposit amount only. So, this the only difference between `Jeonse` and `Wolse` deposits in this app. As it is assumed that you will get the loan for the `Jeonse` where as for `Wolse` you are using your own money.

Monthly loan payment amount is calculated by the formula: `Jeonse` deposit amount * `Jeonse` loan interest rate / 12.

If you find yourself not comprehending what the hell I am talking about, please note that it is about housing rental options in South Korea. More info is https://en.wikipedia.org/wiki/Jeonse.

## Install
1. `git git@github.com:almazkun/jeonse.git`
1. `cd jeonse`
1. `pipenv install`
1. `pipenv run python manage.py migrate`
1. `pipenv run python manage.py runserver`
1. Create a user.
1. Add a new listing.



