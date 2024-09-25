from .base import *  # noqa

INSTALLED_APPS += [  # noqa
    "django_extensions",
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = ["127.0.0.1", "localhost"]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda _: True,
}

# Set this to True for development/testing so tasks run synchronously
CELERY_TASK_ALWAYS_EAGER = True

# Optional: to prevent warnings about task results being stored
CELERY_TASK_EAGER_PROPAGATES = True  # Propagates exceptions in eager tasks
