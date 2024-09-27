import redis

from core.env import env

host = env.str("REDIS_HOST", default="localhost")
port = env.int("REDIS_PORT", default=6379)
db = env.int("REDIS_DB", default=0)
password = env.str("REDIS_PASSWORD", None)

REDIS = redis.Redis(
    host=host,
    port=port,
    db=db,
    password=password,
    decode_responses=True,
)
