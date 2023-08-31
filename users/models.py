from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, null=True, blank=True)
    image = models.ImageField(upload_to="users/", null=True, blank=True, default='default_profile_picture.webp')

    def __str__(self):
        return str(self.user)