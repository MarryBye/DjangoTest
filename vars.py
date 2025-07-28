import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
SETTINGS_FILE = os.getenv('SETTINGS_FILE', 'DjangoPet.settings.default')
