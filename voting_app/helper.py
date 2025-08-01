from flask import g
import redis

def get_redis():
    if 'redis' not in g:
        g.redis = redis.Redis(host="redis", port=6379, db=0)
    return g.redis