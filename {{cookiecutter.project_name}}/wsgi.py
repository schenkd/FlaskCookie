from os import getenv

from app import create_app

app = create_app(getenv('CONFIG') or 'default')
