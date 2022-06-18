from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# class NewUser(AbstractBaseUser):
#     email = models.EmailField(_('email address'), unique=True)
#     user_name = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     start_date = models.DateTimeField(default=timezone.now)
#     phone = PhoneNumberField()
#     ID_number = models.CharField(max_length=150, unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ['user_name']
#
#     def __str__(self):
#         return self.user_name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = PhoneNumberField()
    ID_number = models.CharField(max_length=150, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class CallbackRequest(models.Model):
    name = models.CharField(max_length=150, unique=False)
    id_regex = RegexValidator(regex=r'^\d{8}$', message="ID number must be 8 digits")
    id_number = models.CharField(validators=[id_regex], max_length=8, unique=True)
    # phone = models.CharField(max_length=13)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.") 
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    called = models.BooleanField(default=False)

    def __str__(self):
        return f"Callback request for {self.name}"
