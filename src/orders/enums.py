from django.db import models
from django.utils.translation import gettext as _


class OrderStates(models.TextChoices):
    PENDING = "PENDING", _("Pending")
    COMPLETED = "COMPLETED", _("Completed")
