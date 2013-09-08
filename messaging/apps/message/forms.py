# coding: utf-8
from django import forms

from messaging.apps.message.models import Message


class MessageComposeBroadcastForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('subject', 'content',)


class MessageComposeGroupForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('subject', 'content',)
