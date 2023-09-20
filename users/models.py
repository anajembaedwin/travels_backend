from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    # Add custom fields here
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    # Add groups and user_permissions fields here
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True,
                                   related_name='customuser_set', related_query_name='user')
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user'
    )

    def __str__(self):
        return self.username
