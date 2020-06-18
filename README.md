# yumpizza
Online pizza delivery application.

This is web application for handling a pizza restaurant’s online orders. It is built using django and sqllite.

In this app, a user can
* register and log in/out (necessary when making order)
* access pizza restaurant’s menu, indicate the quantites of pizzas to be ordered
* place the order by providing address and telephone number
* view all previous orders placed by the user

## Technology stack
### Frontend
Bootstrap, HTML, CSS, JQuery
### Backend
Python 3 with Django framework
### Query language
SQLite

## Setup
Clone the git repo, navigate to the directory containig 'yumpizza' folder and follow the below steps
1. Create and activate the virtual environment

    `python3 -m venv venv`
    
    `source venv/bin/activate`
    
2. Install python packages required to run the app (specified in requirements.txt)

    `pip install -r requirements.txt`
    
3. Run the Django app

    `python manage.py runserver`

## Deployment
This website is hosted on an AWS EC2 instance and is available [here](http://18.234.240.229:8000/)
