from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

AUTH_PASSWORD_VALIDATORS = []

CELERY_TASK_ALWAYS_EAGER = True  # To execute tasks synchronously in tests
