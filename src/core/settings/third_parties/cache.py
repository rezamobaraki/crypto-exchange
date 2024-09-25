from core.env import env

host = env.str("REDIS_HOST", default="localhost")
port = env.int("REDIS_PORT", default=6379)

REDIS_LOCATION = f"redis://{host}:{port}"
if password := env.str("REDIS_PASSWORD", None):
    REDIS_LOCATION = f"redis://:{password}@{host}:{port}"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_LOCATION
    }
}
# Cache time to live is 15 minutes by default.
CACHE_TTL = env.int("CACHE_TTL_MINUTES", 15) * 60

DEFAULT_CACHE_TIMEOUT = 60 * 60  # 1 hour in seconds
VOLATILE_CACHE_TIMEOUT = 5 * 60  # 5 minutes in seconds

CACHE_TIMEOUTS = {
    'default': env.int("DEFAULT_CACHE_TIMEOUT", DEFAULT_CACHE_TIMEOUT),
    'volatile': env.int("VOLATILE_CACHE_TIMEOUT", VOLATILE_CACHE_TIMEOUT),
}
