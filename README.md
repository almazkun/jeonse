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

# Aim of this project
In this comprehensive tutorial, we will explore how to build a modern, feature-rich rental listing website using Django, a popular Python web framework, and several community packages. By harnessing the power of packages such as django-allauth, django-tables2, django-htmx, and django-filter, we will create a dynamic and efficient website that offers enhanced functionality and user experience.

Throughout the tutorial, we will guide you through the process of setting up the Django project and integrating these community packages seamlessly. We will demonstrate how django-allauth simplifies user authentication, registration, allowing users to easily sign up, log in, and manage their rental listings.

We will leverage the power of django-tables2 to generate interactive and customizable tables for displaying rental listings, complete with sorting, pagination, and filtering capabilities. By integrating django-htmx, we will implement seamless and efficient user interactions, such as updating listing details, filtering results, and dynamically loading content without full page refreshes, resulting in a smooth and responsive user interface.

To enhance the search functionality, we will utilize django-filter to create advanced filtering options, enabling users to refine their search results based on criteria such as location, price range, amenities, and more.

Throughout the tutorial, we will provide clear and concise instructions, accompanied by code examples and demonstrations of each package's usage. By the end of the tutorial, you will have a fully functional rental listing website that showcases the power of Django and its community packages in creating modern, fast, and feature-rich web applications.

## Tutorial outline:
1. Introduction
    * Overview of the tutorial
    * Explanation of the application's purpose and functionality
2. Prerequisites
    * Django installation
    * Basic understanding of Django and Python
3. Setting up the Project
    * Creating a new Django project
    * Creating a new Django app for rental listings
4. Defining the Models
    * Creating the Listing model
    * Adding fields for title, description, price, location, amenities, etc.
    * Defining the relationships between models (if needed)
1. Database Configuration
    * Configuring the database settings in Django
    * Applying migrations to create the necessary database tables
1. Creating Views and Templates
    * Listing List View: Displaying a list of all rental listings
    * Listing Detail View: Displaying detailed information about a specific rental listing
    * Listing Create View: Allowing users to create new rental listings
    * Listing Update View: Allowing users to modify existing rental listings
1. Building Forms
    * Creating a ListingForm for creating and updating rental listings
    * Implementing form validation and handling form submissions
1. Routing URLs
    * Configuring URL patterns for different views
    * Mapping URLs to appropriate view functions
1. User Authentication and Permissions
    * Implementing user registration and login functionality
    * Restricting certain views or actions to authenticated users
    * Implementing authorization and permissions as required
1. Styling with CSS
    * Adding CSS stylesheets to enhance the application's appearance
    * Applying responsive design principles for better user experience
1. Testing the Application
    * Writing unit tests for models, views, and forms
    * Running tests to ensure the application functions correctly
1. Deployment
    * Preparing the application for deployment
    * Deploying the Django application to a web server or hosting platform (optional)
1. Conclusion
    * Recap of what was covered in the tutorial
    * Encouraging further exploration and enhancements to the application
