# coding: utf-8
from django.test import TestCase

from messaging.apps.message import tasks
from .. import factories


class SendBroadcastMessageTest(TestCase):
    def test_message_is_successfully_sent_to_three_users(self):
        message = factories.MessageF()
        recipients_pks = [factories.UserF().pk for user_index in xrange(3)]

        result = tasks.send_broadcast_message.delay(message.pk)

        self.assertTrue(result.successful())

        self.assertEqual(message.recipients.count(), len(recipients_pks))

    def test_message_is_not_sent_to_sender(self):
        message = factories.MessageF()
        for user_index in xrange(3):
            factories.UserF()

        result = tasks.send_broadcast_message.delay(message.pk)

        self.assertTrue(result.successful())

        has_sender_got_message = message.recipients \
                                        .filter(pk=message.sender_id).exists()
        self.assertFalse(has_sender_got_message)


class SendDirectMessageTest(TestCase):
    def test_message_is_successfully_sent_to_two_users(self):
        message = factories.MessageF()
        recipients_pks = [factories.UserF().pk for user_index in xrange(2)]

        result = tasks.send_direct_message.delay(message.pk, recipients_pks)

        self.assertTrue(result.successful())

        self.assertEqual(message.recipients.count(), len(recipients_pks))


class SendGroupMessageTest(TestCase):
    def test_message_is_successfully_sent_to_group_of_two_people(self):
        message = factories.MessageF()
        group = factories.GroupF()
        recipients_pks = [
            factories.UserF.create(groups=(group,)).pk
            for user_index in xrange(2)
        ]

        result = tasks.send_group_message.delay(message.pk, group.pk)

        self.assertTrue(result.successful())

        self.assertEqual(message.recipients.count(), len(recipients_pks))
