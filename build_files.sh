#!/bin/bash

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Make migrations
python3 manage.py makemigrations

# Apply migrations
python3 manage.py migrate 