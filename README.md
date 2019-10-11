# Django IPL project #
## In this data project we are transforming raw data from IPL into charts that will convey some meaning / analysis. To work on this project we need two csv files matches.csv and deliveries.csv ##

### Download both csv files from https://www.kaggle.com/manasgarg/ipl ###

To plot charts in this project 'matplotlib' is used

### Install Requirements ###
* pip install django
* pip install django-crispy-forms
* pip install django-postgres-copy
* pip install django-redis
* pip install djangorestframework
* pip install psycopg2
* pip install pytz
* pip install redis
* pip install sqlparse
* sudo apt-get install redis-server 

### Following graphs have been generated:- ###

* Plotted a bar chart of the number of matches played per year of all the years in IPL.
* Plotted a stacked bar chart of matches won of all teams over all the years of IPL.
* Plotted a bar chart for the year 2016 extra runs conceded per team.
* Plotted a bar chart For the year 2015 top economical bowlers.