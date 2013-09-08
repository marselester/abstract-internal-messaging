# coding: utf-8
import uuid

from django.conf import settings
from django.db import connection
from django.db.backends.postgresql_psycopg2.base import utc_tzinfo_factory


def create_server_side_cursor(itersize=2000):
    cursor_name = 'namedcursor{}'.format(uuid.uuid4().hex)
    cursor = connection.connection.cursor(name=cursor_name)
    cursor.tzinfo_factory = utc_tzinfo_factory if settings.USE_TZ else None
    cursor.itersize = itersize
    return cursor
