# coding: utf-8
from django.db.models.query import QuerySet

from .redis_ import redis_msg, REDIS_UNREAD_MESSAGES_KEY


class MessageQuerySet(QuerySet):

    def unread_by_user_id(self, user_id):
        messages_pks = redis_msg.smembers(
            REDIS_UNREAD_MESSAGES_KEY.format(user_id=user_id)
        )
        if messages_pks:
            return self.filter(pk__in=messages_pks)
        else:
            return self.none()

    def unread_count_by_user_id(self, user_id):
        messages_pks = redis_msg.smembers(
            REDIS_UNREAD_MESSAGES_KEY.format(user_id=user_id)
        )
        return len(messages_pks)
