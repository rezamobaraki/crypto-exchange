from enum import Enum

from django.utils.translation import gettext_lazy as _


class ErrorMessages(Enum):
    REGISTRATION_FAILED = {
        "message": _("Registration failed. Please check your input and try again."),
        "code": "registration_failed"
    }
    INVALID_CREDENTIALS = {
        "message": _("Invalid credentials provided."),
        "code": "invalid_credential"
    }
    RATE_LIMIT_EXCEEDED = {
        "message": _("Rate limit exceeded. Please try again later."),
        "code": "throttled"
    }
    INSUFFICIENT_BALANCE = {
        "message": _("Insufficient balance."),
        "code": "insufficient_balance"
    }

    @property
    def message(self):
        return self.value["message"]

    @property
    def code(self):
        return self.value["code"]

    def __call__(self):
        return self.message

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message
