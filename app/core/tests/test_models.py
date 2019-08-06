from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def setUp(self):
        self.email = 'example@example.com'
        self.password = 'TestExample123$'

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_new_user_email_normalized(self):
        """ Test the normalized email for a new user """
        email = 'example@EXAMPLE.COM'
        user = get_user_model().objects.create_user(email, self.password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            '123test'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
