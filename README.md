# Django Dwich Project

This is a Django project for Dwich&Co restaurant.



## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


## Prerequisites

Make sure you have the following installed:

- [Python 3.12](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)


## Installation

Follow these steps to get a development environment running:


### Clone the repository

```bash
git clone https://github.com/Darkblue5031/Dwich-Co
```


### Create a virtual environment

Navigate into the project directory:

```bash
cd your_project
```


### Create a virtual environment using venv:

```bash
python3 -m venv env
```


### Activate the virtual environment

- On macOS/Linux:

```bash
source env/bin/activate
```
- On Windows:

```bash
.\env\Scripts\activate
```


### Install dependencies

Install the required packages using pip:

```bash
pip install -r Requirements.txt
```


## Usage
Follow these steps to run the Django project:


### Create a superuser to access the admin panel:

```bash
cd Dwich
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### Make migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### Run the development server

Start the Django development server:

```bash
python manage.py runserver
```
Access the development server at http://localhost:8000/.

Access the admin panel

Navigate to http://localhost:8000/admin/ in your browser and log in with the superuser credentials you created earlier.

Add manually now yours products and run populate_db script to create associated menus.

This project is not ended !