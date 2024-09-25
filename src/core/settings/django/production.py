from .base import *  # noqa

DEBUG = False

SECRET_KEY = env.str("SECRET_KEY")  # noqa

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])  # noqa
