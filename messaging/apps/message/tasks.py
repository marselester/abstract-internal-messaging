# coding: utf-8
import celery
from django.contrib.auth.models import User

from .models import Message


@celery.task
def send_broadcast_message(message_pk):
    try:
        message = Message.objects.get(pk=message_pk)
    except Message.DoesNotExist as exc:
        raise celery.current_task.retry(exc=exc)

    message.send_to(User.objects.exclude(pk=message.sender_id))


@celery.task
def send_direct_message(message_pk, recipients_pks):
    try:
        message = Message.objects.get(pk=message_pk)
    except Message.DoesNotExist as exc:
        raise celery.current_task.retry(exc=exc)

    message.send_to(User.objects.filter(pk__in=recipients_pks))


@celery.task
def send_group_message(message_pk, group_pk):
    try:
        message = Message.objects.get(pk=message_pk)
    except Message.DoesNotExist as exc:
        raise celery.current_task.retry(exc=exc)

    message.send_to(User.objects.filter(groups=group_pk))
