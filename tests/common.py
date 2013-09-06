# coding: utf-8


class ViewTestMixin(object):

    def _test_sign_in_redirect_url(self, response, url):
        login_url = '/accounts/login/?next={}'.format(url)
        self.assertRedirects(response, login_url)
