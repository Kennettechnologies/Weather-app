#!/bin/bash

# Install Python dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

# Apply migrations
python3 manage.py migrate --noinput 