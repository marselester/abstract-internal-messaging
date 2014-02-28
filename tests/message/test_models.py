# coding: utf-8
from django.test import TestCase
from django.contrib.auth.models import User

from .. import factories


class MessageSendToTest(TestCase):
    def test_message_is_sent_to_five_users(self):
        message = factories.MessageF()
        recipients_pks = [factories.UserF().pk for user_index in xrange(5)]

        users_except_sender = User.objects.exclude(pk=message.sender_id)
        message.send_to(users_except_sender)

        self.assertEqual(message.recipients.count(), len(recipients_pks))
