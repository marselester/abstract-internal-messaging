# coding: utf-8
from django_webtest import WebTest

from ..common import ViewTestMixin


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

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/inbox/mark_as_read/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)


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

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/compose/direct/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)


class MessageComposeBroadcastTest(ViewTestMixin, WebTest):

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/compose/broadcast/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)


class MessageComposeGroupTest(ViewTestMixin, WebTest):

    def test_404_when_message_pk_is_non_arabic_numeral(self):
        # ``\d`` regex is valid for "๓".
        thai_number_four = '๓'
        url = '/messages/compose/group/{}/'.format(thai_number_four)

        self.app.get(url, status=404)

    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/messages/compose/group/1/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)
