# coding: utf-8
import autocomplete_light
from django import forms
from django.contrib.auth.models import User

from messaging.apps.message.models import Message


class MessageComposeForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('subject', 'content',)


class UserAutocomplete(autocomplete_light.AutocompleteModelBase):

    search_fields = ['^first_name', 'last_name']

autocomplete_light.register(User, UserAutocomplete)


class MessageComposeDirectForm(MessageComposeForm):

    recipients = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete_light.MultipleChoiceWidget('UserAutocomplete')
    )
