"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """"Test models."""

    def test_create_user_with_email_successful(self):
        """Test create a user with an email is successfully"""
        email = 'test@example.com'
        password = 'testpass123'
        firstname = 'fname'
        middlename = 'mname'
        lastname = 'lname'
        contact = '09679016893'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            contact=contact,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
