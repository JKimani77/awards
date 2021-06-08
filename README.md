# Ahwards
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![codebeat badge](https://codebeat.co/badges/7283d5cd-8963-4679-844b-a5c915ab09e0)]
## Description
This a web application built using Python, Django and Postgresql.The app is a clone  of the Awwwards app, where users can view projects posted and rate them. The applicationa also has a functioning authentication system and a profile page.


## Author

Joshua Kimani

## Link to site
https://ahwards.herokuapp.com/

## DB diagram
![Ahwards](https://github.com/JKimani77/awards/blob/master/raw/db.png?raw=true)


## API Reference

#### Get all profile objects

```http
  GET /api/profile
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get profile object by id

```http
  GET /api/profile/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |



## User Stories

A user can register and login
![DBDIAGRAM](https://github.com/JKimani77/awards/blob/master/raw/login.png?raw=true)

A user can create their own profile to be able to post
![DBDIAGRAM](https://github.com/JKimani77/awards/blob/master/raw/profile.png?raw=true)

A user can View Projects posted and rate them
![DBDIAGRAM](https://github.com/JKimani77/awards/blob/master/raw/viewposted.png?raw=true)

A user can visit the wevbsite link.
![DBDIAGRAM](https://github.com/JKimani77/awards/blob/master/raw/gotosite.png?raw=true)

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
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`
`MODE`
`DATABASE_URL`
`DEBUG`
`DB_NAME`
`DB_USERNAME`
`DB_PASSWORD`
`DB_PORT`
`ALLOWED_HOSTS`

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

  ---You will need to change the database_url env variable to your local database or change your mode to 'dev and configure the database evnironment vars.'
  
```bash
    $ python3 manage.py test
```
## Known Bugs


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

Reach me at jkkimani77@gmail.com

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

