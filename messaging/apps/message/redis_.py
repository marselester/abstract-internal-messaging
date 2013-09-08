# coding: utf-8
import redis
from django.conf import settings


redis_msg = redis.from_url(url=settings.MESSAGE_APP_REDIS_URL,
                           db=settings.MESSAGE_APP_REDIS_DB)
