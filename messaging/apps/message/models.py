# coding: utf-8
from django.db import models, transaction, IntegrityError, connection
from django.contrib.auth.models import User

from messaging.common.db import create_server_side_cursor


NEW_RECIPIENT_OF_MESSAGE_SQL = '''
INSERT INTO message_recipients (message_id, user_id)
VALUES (%s, %s)
'''


class Message(models.Model):

    sender = models.ForeignKey(User, related_name='sent_messages')
    recipients = models.ManyToManyField(User, related_name='inbox',
                                        db_table='message_recipients')
    recipients_qty = models.PositiveIntegerField(blank=True, default=0)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    datetime_created = models.DateTimeField(auto_now=True)

    @transaction.atomic
    def send_to(self, recipients_qs):
        regular_cursor = connection.cursor()
        named_cursor = create_server_side_cursor()

        users_ids_sql = str(recipients_qs.values_list('id', flat=True).query)
        named_cursor.execute(users_ids_sql)

        for row in named_cursor:
            user_id = row[0]
            try:
                with transaction.atomic():
                    regular_cursor.execute(NEW_RECIPIENT_OF_MESSAGE_SQL,
                                           (self.id, user_id))
            except IntegrityError:
                # TODO: log it.
                pass
