# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    sender = models.ForeignKey(User, related_name='sent_messages')
    recipients = models.ManyToManyField(User, related_name='inbox',
                                        db_table='message_recipients')
    recipients_qty = models.PositiveIntegerField(blank=True, default=0)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    datetime_created = models.DateTimeField(auto_now=True)
