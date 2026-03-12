import json
import redis
from app.core.config import settings

_client = None

def get_redis():
    global _client
    if _client is None:
        try:
            _client = redis.Redis.from_url(settings.redis_url, decode_responses=True)
            _client.ping()
        except Exception:
            _client = False
    return _client if _client else None

def get_json(key: str):
    client = get_redis()
    if not client:
        return None
    value = client.get(key)
    if not value:
        return None
    return json.loads(value)

def set_json(key: str, value, ex: int = 60):
    client = get_redis()
    if not client:
        return
    client.set(key, json.dumps(value, default=str), ex=ex)

def delete_key(key: str):
    client = get_redis()
    if not client:
        return
    client.delete(key)
