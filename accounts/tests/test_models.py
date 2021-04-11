from django.contrib.auth import get_user_model
from django.test import TestCase


class UserModelTestCase(TestCase):
    """Tests for the custom user model

    Args:
        TestCase (object): A subclass of django.test.TransactionTestCase
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.User = get_user_model()

        # create a normal user
        cls.user = cls.User.objects.create_user(
            first_name='Normal',
            last_name='User',
            email='normal@user.com',
            phone_number='+2540110234567',
            password='foo'
        )

    # email
    def test_email_label(self):
        email__meta = self.user._meta.get_field('email')
        self.assertEqual(email__meta.verbose_name, 'email address')

    def test_email_can_not_save_NULL_in_the_database(self):
        email__meta = self.user._meta.get_field('email')
        self.assertEqual(email__meta.null, False)

    def test_email_is_not_allowed_to_be_blank(self):
        email__meta = self.user._meta.get_field('email')
        self.assertEqual(email__meta.blank, False)

    # first name
    def test_first_name_label(self):
        first_name__meta = self.user._meta.get_field('first_name')
        self.assertEqual(first_name__meta.verbose_name, 'first name')

    def test_first_name_max_length(self):
        first_name__meta = self.user._meta.get_field('first_name')
        self.assertEqual(first_name__meta.max_length, 30)

    def test_first_name_can_not_save_NULL_in_the_database(self):
        first_name__meta = self.user._meta.get_field('first_name')
        self.assertEqual(first_name__meta.null, False)

    def test_first_name_is_not_allowed_to_be_blank(self):
        first_name__meta = self.user._meta.get_field('first_name')
        self.assertEqual(first_name__meta.blank, False)

    def test_last_name_label(self):
        last_name__meta = self.user._meta.get_field('last_name')
        self.assertEqual(last_name__meta.verbose_name, 'last name')

    def test_last_name_max_length(self):
        last_name__meta = self.user._meta.get_field('last_name')
        self.assertEqual(last_name__meta.max_length, 30)

    def test_last_name_can_not_save_NULL_in_the_database(self):
        last_name__meta = self.user._meta.get_field('last_name')
        self.assertEqual(last_name__meta.null, False)

    def test_last_name_is_not_allowed_to_be_blank(self):
        last_name__meta = self.user._meta.get_field('last_name')
        self.assertEqual(last_name__meta.blank, False)

    def test_phone_number_label(self):
        phone_number__meta = self.user._meta.get_field('phone_number')
        self.assertEqual(phone_number__meta.verbose_name, 'phone number')

    def test_phone_number_max_length(self):
        phone_number__meta = self.user._meta.get_field('phone_number')
        self.assertEqual(phone_number__meta.max_length, 20)

    def test_phone_number_help_text(self):
        phone_number__meta = self.user._meta.get_field('phone_number')
        self.assertEqual(phone_number__meta.help_text,
            'Enter a valid phone number'
        )

    def test_phone_number_can_not_save_NULL_in_the_database(self):
        phone_number__meta = self.user._meta.get_field('phone_number')
        self.assertEqual(phone_number__meta.null, False)

    def test_phone_number_is_not_allowed_to_be_blank(self):
        phone_number__meta = self.user._meta.get_field('phone_number')
        self.assertEqual(phone_number__meta.blank, False)

    def test_bio_label(self):
        bio__meta = self.user._meta.get_field('bio')
        self.assertEqual(bio__meta.verbose_name, 'bio')

    def test_bio_max_length(self):
        bio__meta = self.user._meta.get_field('bio')
        self.assertEqual(bio__meta.max_length, 1000)

    def test_bio_help_text(self):
        bio__meta = self.user._meta.get_field('bio')
        self.assertEqual(bio__meta.help_text,
            'Enter a brief summary of yourself'
        )

    def test_bio_can_save_NULL_in_the_database(self):
        bio__meta = self.user._meta.get_field('bio')
        self.assertEqual(bio__meta.null, True)

    def test_bio_is_allowed_to_be_blank(self):
        bio__meta = self.user._meta.get_field('bio')
        self.assertEqual(bio__meta.blank, True)

    def test_profile_picture_label(self):
        profile_picture__meta = self.user._meta.get_field('profile_picture')
        self.assertEqual(profile_picture__meta.verbose_name,
            'profile picture'
        )

    def test_the_default_profile_picture(self):
        profile_picture__meta = self.user._meta.get_field('profile_picture')
        self.assertEqual(profile_picture__meta.default,
            'default.png'
        )

    def test_where_profile_pictures_are_uploaded_to(self):
        profile_picture__meta = self.user._meta.get_field('profile_picture')
        self.assertEqual(profile_picture__meta.upload_to,
            'profile_pictures'
        )

    def test_profile_picture_can_not_save_NULL_in_the_database(self):
        profile_picture__meta = self.user._meta.get_field('profile_picture')
        self.assertEqual(profile_picture__meta.null, False)

    def test_profile_picture_is_not_allowed_to_be_blank(self):
        profile_picture__meta = self.user._meta.get_field('profile_picture')
        self.assertEqual(profile_picture__meta.blank, False)

    def test_object_name_is_first_name(self):
        self.assertEqual(self.user.first_name, str(self.user))
