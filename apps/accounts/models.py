from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """Helps Django work with our custom user Model"""
    def create_user(self, email, groups_id, password=None):
        if not email:
            raise ValueError('Users must have an email address.')
        email = self.normalize_email(email)
        user = self.model(email=email, groups_id=groups_id)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, groups_id, password):
        """ Creates and saves a new superuser with given details."""
        user = self.create_user(email, groups_id, password)
        
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user
    
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['groups_id']
    objects = UserManager()
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name
                                         
    def __str__(self):
        return self.email
