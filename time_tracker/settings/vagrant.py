DEBUG = True
SECRET_KEY = 'notasecret'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'time_tracker',
        'USER': 'vagrant',
    }
}
