from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, *args, **kwargs):
    print("sender", sender)
    print('instance', instance)
    print('instane_id', instance.id)
    print('created', created)
    if created:
        Token.objects.create(user=instance)
