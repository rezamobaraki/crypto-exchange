# Set the default Django settings module for the 'celery' program.
import os

from celery import Celery

from core.env import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.local')

host = env.str("REDIS_HOST", default="localhost")
port = env.int("REDIS_PORT", default=6379)
password = env.str("REDIS_PASSWORD", default=None)
celery_db = env.int("REDIS_CELERY_DB", default=1)
if password:
    redis_url = f"redis://:{password}@{host}:{port}/{celery_db}"  # noqa
else:
    redis_url = f"redis://{host}:{port}/{celery_db}"  # noqa

celery_app = Celery('crypto-exchange', broker=redis_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Use the Django database scheduler
celery_app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

# Load task modules from all registered Django apps.
celery_app.autodiscover_tasks()

celery_app.conf.task_store_errors_even_if_ignored = True

# Set broker_connection_retry_on_startup to True
celery_app.conf.broker_connection_retry_on_startup = True

# Load scheduled tasks.
celery_app.conf.beat_schedule = {}
