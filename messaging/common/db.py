# coding: utf-8
import uuid

from django.conf import settings
from django.db import connection
from django.db.backends.postgresql_psycopg2.base import utc_tzinfo_factory


def create_server_side_cursor(itersize=2000):
    """Creates and returns PostgreSQL named server side cursor.

    Iterating through a large Django QuerySet consumes massive amounts
    of memory. Rather than executing a whole query at once, it is
    possible to set up a cursor that encapsulates the query, and then
    read the query result a few rows at a time.

    http://initd.org/psycopg/docs/usage.html#server-side-cursors

    """
    cursor_name = 'namedcursor{}'.format(uuid.uuid4().hex)
    cursor = connection.connection.cursor(name=cursor_name)
    cursor.tzinfo_factory = utc_tzinfo_factory if settings.USE_TZ else None
    cursor.itersize = itersize
    return cursor
