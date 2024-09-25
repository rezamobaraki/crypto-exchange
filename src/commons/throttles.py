from rest_framework.throttling import SimpleRateThrottle


class BaseRateThrottle(SimpleRateThrottle):
    def get_cache_key(self, request, view):
        ident = request.user.pk if request.user.is_authenticated else self.get_ident(request)
        return self.cache_format % {'scope': self.scope, 'ident': ident}


class AuthenticationRateThrottle(BaseRateThrottle):
    scope = 'authentication'
