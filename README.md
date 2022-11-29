# Overview

Simple RestFul api build with DJango

## Setup

```bash
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependency
pip3 install -r requirements.txt

# create super-admins
python3 manage.py createsuperuser

#
python3 manage.py migrate
python3 manage.py runserver

# Run withn Daphne
daphne server.asgi:application
```
