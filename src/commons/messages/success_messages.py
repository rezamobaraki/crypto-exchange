from enum import Enum

from django.utils.translation import gettext_lazy as _


class SuccessMessages(Enum):
    REGISTRATION_SUCCESS = {
        "message": _("User registered successfully. Please log in to continue."),
        "code": "registration_success"
    }

    @property
    def message(self):
        return self.value["message"]

    @property
    def code(self):
        return self.value["code"]
