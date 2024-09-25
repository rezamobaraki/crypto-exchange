import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    username = factory.Faker('user_name')
    password = factory.PostGenerationMethodCall('set_password', 'new_password')
