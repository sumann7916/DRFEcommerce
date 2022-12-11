from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=30, null=True)
    company_name = models.CharField(blank=True, null = True, max_length=100)
    USER_TYPE_CHOICES = (
      (1, 'seller'),
      (2, 'buyer'),
      (3, 'admin'),
  )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)

    def __str__(self):
        if self.user_type == 1:
            return self.company_name
        else:
            return self.first_name + " " + self.last_name



