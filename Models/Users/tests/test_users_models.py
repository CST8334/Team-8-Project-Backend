from django.test import TestCase
from Models.Users.models import *


class UsersTestCase(TestCase):
    def setUp(self):
        Users.objects.create(user_type="Creator", email="test@cmail.com", password="testPass", organization_id=321,
                             user_role="user", description="test generated user")

    def test_users_created(self):
        """
        Users models are successfully created
        """
        user_test = Users.objects.get(id=1)
        self.assertEqual(user_test.user_type, "Creator")
        self.assertEqual(user_test.email, "test@cmail.com")
        #self.assertEqual(user_test.password, "testPass")
        self.assertEqual(user_test.organization_id, 321)
        self.assertEqual(user_test.user_role, "user")
        self.assertEqual(user_test.description, "test generated user")
