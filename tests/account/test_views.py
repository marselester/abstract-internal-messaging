# coding: utf-8
from django_webtest import WebTest

from .. import factories
from ..common import ViewTestMixin


class DashboardTest(ViewTestMixin, WebTest):
    def test_redirect_to_login_page_when_user_is_not_logged_in(self):
        url = '/'

        response = self.app.get(url)

        self._test_sign_in_redirect_url(response, url)

    def test_user_successfully_signed_in(self):
        user = factories.UserF()

        response = self.app.get('/', user=user, status=200)

        expected_welcome = 'Hello, {}'.format(user.username)
        self.assertContains(response, expected_welcome)
