from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

# Create your models here.


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        if not email:
            raise ValueError("You must provide an email")
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(("email address"), blank=False, unique=True)
    avatar = models.ImageField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = UserAccountManager()

    def __str__(self):
        if self.first_name != "":
            return self.first_name + " " + self.last_name
        else:
            return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField("self", blank=True, null=True, symmetrical=False)
    cover_page = models.ImageField(blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True, null=True)
    location = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.user.username + "'s" + " Profile"


class Preferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
