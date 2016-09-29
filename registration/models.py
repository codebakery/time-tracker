from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager as DefaultUserManager
from django.db import models


class UserManager(DefaultUserManager):
    def _create_user(self, username, password, **kwargs):
        user = User.objects.create(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, username, password, **kwargs):
        return self._create_user(username, password, **kwargs)
    
    def create_superuser(self, username, password, **kwargs):
        return self._create_user(username, password, is_staff=True, is_superuser=True, **kwargs)
    

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=40, blank=False, unique=True)  # TODO: Username unique only in combinations with company
    email = models.EmailField(blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Django internals 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    # MANAGERS
    objects = UserManager()
    
    # Django required
    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
