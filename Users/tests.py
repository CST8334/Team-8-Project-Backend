from django.test import TestCase
from Users.models import CustomUser
from Users.models import UserInvitation

"""
Model test cases
"""


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(user_type="Creator", email="test@tmail.com", password="testPass", organization_id=123,
                                  user_role="user", description="test generated user", googleId='', googleName='',
                                  googleEmail='', instagramId='', instagramUser='', instagramName='', tiktokId='',
                                  tiktokEmail='')

    def test_email_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email address')

    def test_user_type_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('user_type').verbose_name
        self.assertEqual(field_label, 'user type')

    def test_organization_id_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('organization_id').verbose_name
        self.assertEqual(field_label, 'organization id')

    def test_creation_time_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')

    def test_user_role_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('user_role').verbose_name
        self.assertEqual(field_label, 'user role')

    def test_description_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_googleId_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('googleId').verbose_name
        self.assertEqual(field_label, 'googleId')

    def test_googleName_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('googleName').verbose_name
        self.assertEqual(field_label, 'googleName')

    def test_googleEmail_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('googleEmail').verbose_name
        self.assertEqual(field_label, 'googleEmail')

    def test_instagramId_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('instagramId').verbose_name
        self.assertEqual(field_label, 'instagramId')

    def test_instagramUser_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('instagramUser').verbose_name
        self.assertEqual(field_label, 'instagramUser')

    def test_instagramName_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('instagramName').verbose_name
        self.assertEqual(field_label, 'instagramName')

    def test_tiktokId_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('tiktokId').verbose_name
        self.assertEqual(field_label, 'tiktokId')

    def test_tiktokEmail_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('tiktokEmail').verbose_name
        self.assertEqual(field_label, 'tiktokEmail')

    def test_object_name(self):
        user = CustomUser.objects.get(id=1)
        expected_name = f'{user.email}'
        self.assertEqual(str(user), expected_name)


class UserInvitationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserInvitation.objects.create(invitation_code=CustomUser.objects.generate_new_invite_code())

    def test_invitation_code_label(self):
        invitation_code = UserInvitation.objects.get(id=1)
        field_label = invitation_code._meta.get_field('invitation_code').verbose_name
        self.assertEqual(field_label, 'invitation code')

    def test_is_used_label(self):
        invitation_code = UserInvitation.objects.get(id=1)
        field_label = invitation_code._meta.get_field('is_used').verbose_name
        self.assertEqual(field_label, 'is used')

    def test_invitation_code_max_length(self):
        invitation_code = UserInvitation.objects.get(id=1)
        max_length = invitation_code._meta.get_field('invitation_code').max_length
        self.assertEqual(max_length, 25)


"""
View test cases
"""
