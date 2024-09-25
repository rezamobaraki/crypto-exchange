from django.utils.translation import gettext as _


class LogMessages:
    REGISTRATION_ATTEMPT = _("Attempted registration with username: {}")
    FAILED_LOGIN_ATTEMPT = _("Failed login attempt for username: {}")

    @classmethod
    def register_existing_user(cls, username):
        return cls.REGISTRATION_ATTEMPT.format(username)

    @classmethod
    def login_fail(cls, username):
        return cls.FAILED_LOGIN_ATTEMPT.format(username)
