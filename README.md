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
1. `cp .env.example .env`
1. `pipenv install`
1. `pipenv run python manage.py migrate`
1. `pipenv run python manage.py runserver`
1. Create a user.
1. Add a new listing.


## Tutorial
* django setup
```bash
pipenv install django==4.2.2
pipenv shell
django-admin startproject settings .
python manage.py startapp jeonse
python manage.py migrate
python manage.py runserver
```

* modify settings.py
```python
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    ...
    "jeonse",
    ...
]

# DJANGO-ALLAUTH CONFIGS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "home"
# https://django-allauth.readthedocs.io/en/latest/views.html#logout-account-logout
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
# https://django-allauth.readthedocs.io/en/latest/installation.html?highlight=backends
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"


# STATIC FILES

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [BASE_DIR / "static"]

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-STATIC_ROOT
STATIC_ROOT = BASE_DIR / "staticfiles"

# https://whitenoise.evans.io/en/stable/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

```


docker run --env-file .env --rm -p 8001:8000 --name jeonse jeonse:latest