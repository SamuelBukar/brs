#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Create a new Django project
django-admin startproject myproject

# Navigate into the project directory
cd myproject

# Create a new Django app
python manage.py startapp myapp

# Apply initial migrations
python manage.py migrate

echo "Django project setup complete."
