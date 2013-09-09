# coding: utf-8
from django_webtest import WebTest

from ..common import ViewTestMixin
from .. import factories


class MessageShowTest(ViewTestMixin, WebTest):

    def test_404_when_message_pk_is_non_arabic_numeral(self):
        # ``\d`` regex is valid for "๓".
        thai_number_four = '๓'
        url = '/messages/{}/'.format(thai_number_four)

        self.app.get(url, status=404)

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/1/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)


class MessageInboxTest(ViewTestMixin, WebTest):

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/inbox/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)


class MessageMarkAsReadTest(ViewTestMixin, WebTest):

    url = '/messages/inbox/mark_as_read/'
    dashboard_url = '/'
    csrf_checks = False

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        response = self.app.get(self.url)

        self._test_sign_in_redirect_url(response, self.url)

    def test_404_when_message_is_not_found(self):
        user = factories.UserF()

        self.app.post(self.url, user=user, status=404)

    def test_message_is_successfully_marked_as_read(self):
        user = factories.UserF()
        params = {
            'message_pk': factories.MessageF().pk
        }

        response = self.app.post(self.url, params, user=user)

        self.assertRedirects(response, self.dashboard_url)
        self.assertContains(response.follow(), 'Message was marked as read')


class MessageDeleteTest(ViewTestMixin, WebTest):

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/inbox/delete/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)


class MessageSentTest(ViewTestMixin, WebTest):

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/sent/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)


class MessageComposeDirectTest(ViewTestMixin, WebTest):

    url = '/messages/compose/direct/'
    dashboard_url = '/'

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        response = self.app.get(self.url)

        self._test_sign_in_redirect_url(response, self.url)

    def test_message_is_successfully_sent(self):
        user = factories.UserF()
        recipient = factories.UserF()

        response = self.app.get(self.url, user=user)

        form = response.forms['compose-direct-message-form']
        form['recipients'].force_value([recipient.pk])
        form['subject'] = 'hi'
        form['content'] = 'How are you?'
        response = form.submit()

        self.assertRedirects(response, self.dashboard_url)
        self.assertContains(response.follow(), 'Direct message was sent')


class MessageComposeBroadcastTest(ViewTestMixin, WebTest):

    url = '/messages/compose/broadcast/'
    dashboard_url = '/'

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        response = self.app.get(self.url)

        self._test_sign_in_redirect_url(response, self.url)

    def test_message_is_successfully_sent(self):
        user = factories.UserF()

        response = self.app.get(self.url, user=user)

        form = response.forms['compose-broadcast-message-form']
        form['subject'] = 'hi'
        form['content'] = 'How are you?'
        response = form.submit()

        self.assertRedirects(response, self.dashboard_url)
        self.assertContains(response.follow(), 'Broadcast message was sent')


class MessageComposeGroupTest(ViewTestMixin, WebTest):

    dashboard_url = '/'

    def test_404_when_message_pk_is_non_arabic_numeral(self):
        # ``\d`` regex is valid for "๓".
        thai_number_four = '๓'
        url = '/messages/compose/group/{}/'.format(thai_number_four)

        self.app.get(url, status=404)

    def test_404_when_group_is_not_found(self):
        user = factories.UserF()
        url = '/messages/compose/group/1/'

        self.app.get(url, user=user, status=404)

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        group = factories.GroupF()
        url = '/messages/compose/group/{}/'.format(group.pk)

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)

    def test_message_is_successfully_sent(self):
        group = factories.GroupF()
        for user_index in xrange(2):
            factories.UserF.create(groups=(group,)).pk
        url = '/messages/compose/group/{}/'.format(group.pk)
        user = factories.UserF()

        response = self.app.get(url, user=user)

        form = response.forms['compose-group-message-form']
        form['subject'] = 'hi'
        form['content'] = 'How are you?'
        response = form.submit()

        self.assertRedirects(response, self.dashboard_url)
        self.assertContains(response.follow(), 'Group message was sent')
