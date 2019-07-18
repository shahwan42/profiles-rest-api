from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError("User must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details.
        This method is used when you run `./manage.py createsuperuser` command"""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system."""

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # the default login field
    USERNAME_FIELD = "email"
    # the requried fields besides the USERNAME_FIELD
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        """Use to get a user's full name."""

        return self.name

    def get_short_name(self):
        """Use to get a user's short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update."""
    user_profile = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as string"""

        return self.status_text
