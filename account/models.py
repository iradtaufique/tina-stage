from django.db import models
from django.contrib.auth.models import AbstractUser


class Sectors(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    is_sectorIT = models.BooleanField('sectorIT', default=False)
    is_ITManager = models.BooleanField('ITManager', default=False)
    sector = models.ForeignKey(Sectors, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)




