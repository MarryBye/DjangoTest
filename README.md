# Pet project on Django for self education

Setup

1. Create virtual environment

Windows
``
python -m venv .venv
./.venv/Scripts/Activate.ps1
``

Linux/MacOS
``
python3 -m venv .venv
source ./.venv/bin/activate
``

2. Install dependencies

Windows
``pip install -r requirements.txt``

Linux/MacOS
``pip3 install -r requirements.txt``

3. Need 2 environment variables:
``SECRET_KEY`` - secret key for yout application
``SETTINGS_FILE`` - which settings file must be used for project (for example ``DjangoPet.settings.default.py``)

Can be set with .env file

4. Make migrations and apply them

``
python manage.py makemigrations
python manage.py migrate
``

Ready to use!

I used the django-liverelod, so you can start it and see your changes on site in realtime!

As a bonus, i created launch.json and tasks.json with ready-to-use commands for work in VSCode!

This project is not ready and used as education project.