import factory

from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'User{0}@fc.tr'.format(n))
    password = factory.PostGenerationMethodCall('set_password', '1234')
    username = factory.Sequence(lambda n: 'factory_{}'.format(n))
