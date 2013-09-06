# coding: utf-8
import factory
from django.contrib.auth.models import User


class UserF(factory.DjangoModelFactory):

    FACTORY_FOR = User

    username = factory.Sequence(lambda num: u'jon_snow{}'.format(num))
    first_name = factory.Sequence(lambda num: u'Jon{}'.format(num))
    last_name = factory.Sequence(lambda num: u'Snow{}'.format(num))
    email = factory.LazyAttribute(
        lambda obj: u'{}@example.org'.format(obj.username))
    is_staff = True
    is_active = True
    is_superuser = False
    password = '123'

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserF, cls)._prepare(create, **kwargs)

        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
