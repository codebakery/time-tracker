import os
from django.core.exceptions import ImproperlyConfigured


def get_env_var(var_name, default=None):
    """
    Get the environmental variable or throw an exception.
    """
    try:
        return os.environ[var_name]
    except KeyError:
        message = '{} envorinmental variable is missing'.format(var_name)
        raise ImproperlyConfigured(message)

ALLOWED_HOSTS = [
    'time-tracker.codebakery.io'
]

DEBUG = False
SECRET_KEY = get_env_var('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'time_tracker',
        'USER': 'uwsgi',
    }
}
