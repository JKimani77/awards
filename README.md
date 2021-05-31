# Ahwards
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![codebeat badge](https://codebeat.co/badges/7283d5cd-8963-4679-844b-a5c915ab09e0)]
## Description
This a web application built using Python, Django and Postgresql.The app is a clone  of the Awwwards app, where users can view projects posted and rate them. The applicationa also has a functioning authentication system and a profile page.


## Author

Joshua Kimani

##Link to site
![Go]( https://ahwards.herokuapp.com/)

## DB diagram
![Ahwards](https://github.com/JKimani77/awards/blob/master/raw/db.png?raw=true)



# Installation

## Clone
    
```bash
    git clone https://github.com/JKimani77/awards.git
    
```
##  Create virtual environment
```bash
    python3.6 -m venv --without-pip virtual
    
```
## Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```
## Run initial migration
```bash
   $ python3.6 manage.py makemigrations awards
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```

## Test class

```bash
    $ python3 manage.py test
```
## Known Bugs


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Python Shell
    Python 3.6
    Django
    Bootstrap Materialize
    HTML
    CSS
    PostgreSQL
    Django Rest Framework

## |||||||||||

    All rights reserved. 

