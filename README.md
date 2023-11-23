# # Movie Web App (Django)

A full responsive website for Movie app using the django framework

## Overview

This project is a responsive website for a Movie app built using the Django web framework. It allows users to get information about movies. This app is created using popular movie database api and we can update web app to the recent data using single command.

## Features

- API to get the movie data
- single command to update the database
- Website will dynamically created each and every time when database get updated
- Responsive Design
- Paginator are used for pagination of web app
- all table are connected to database

## Installation
1. Clone the Repository
   - git clone https://github.com/purushoth110797/movie-app.git
   - cd movie-app
3. Create the virtual Environment
   - python -m venv venv
4. Activate the Virtual Environment
   - venv\Scripts\activate
5. Install dependencies
   - pip install -r requirements.txt
6. Apply Migrations
   - python manage.py migrate

## Usage

1. python manage.py runserver

2. The application will be accessible at http://127.0.0.1:8000/ by default.

3. To access the Admin Pannel
   - python manage.py createsuperuser
   - Visit http://127.0.0.1:8000/admin/
4. Explore the Website:
  - Open your browser and go to http://127.0.0.1:8000/ to explore the movie website.

## Technologies
- Django framework
- Python
- HTML
- CSS
- JavaScript

## Contributors

- [Purushothaman](https://github.com/purushoth110797)

## License

This project is open-source.

## Acknowledgments

- 
