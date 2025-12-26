from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        print("SIGNAL FIRED", instance)
